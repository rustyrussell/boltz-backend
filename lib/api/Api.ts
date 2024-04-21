import cors from 'cors';
import express, { Application, NextFunction, Request, Response } from 'express';
import { ApiConfig } from '../Config';
import Logger from '../Logger';
import CountryCodes from '../service/CountryCodes';
import Service from '../service/Service';
import Controller from './Controller';
import { errorResponse } from './Utils';
import ApiV2 from './v2/ApiV2';
import WebSocketHandler from './v2/WebSocketHandler';

class Api {
  private app: Application;
  private readonly websocket: WebSocketHandler;
  private readonly controller: Controller;

  constructor(
    private readonly logger: Logger,
    private readonly config: ApiConfig,
    service: Service,
    countryCodes: CountryCodes,
  ) {
    this.app = express();
    this.app.set('trust proxy', 'loopback');

    if (config.cors === undefined || config.cors.length !== 0) {
      this.app.use(
        cors({
          origin: config.cors || '*',
          methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
          preflightContinue: false,
          optionsSuccessStatus: 204,
        }),
      );
    }

    this.app.use(
      express.json({
        verify(req, _, buf: Buffer, encoding: string) {
          if (buf && buf.length) {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            req.rawBody = buf.toString((encoding as BufferEncoding) || 'utf-8');
          }
        },
      }),
    );

    // Catch the ugly errors generated by the body-parser
    this.app.use(
      (error: any, req: Request, res: Response, next: NextFunction) => {
        if (error instanceof SyntaxError) {
          errorResponse(logger, req, res, error);
          return;
        }

        next(error);
      },
    );

    this.controller = new Controller(logger, service, countryCodes);
    this.websocket = new WebSocketHandler(service, this.controller);

    new ApiV2(
      this.logger,
      service,
      this.controller,
      countryCodes,
    ).registerRoutes(this.app);
    this.registerRoutes(this.controller);
  }

  public init = async (): Promise<void> => {
    await this.controller.init();

    await new Promise<void>((resolve) => {
      const server = this.app.listen(this.config.port, this.config.host, () => {
        this.logger.info(
          `API server listening on: ${this.config.host}:${this.config.port}`,
        );
        this.websocket.register(server);
        resolve();
      });
    });
  };

  private registerRoutes = (controller: Controller) => {
    // Static files
    ['/', '/index.html'].forEach((path) => {
      this.app.route(path).get(controller.serveFile('index.html'));
    });
    this.app.route('/favicon.ico').get(controller.serveFile('favicon.ico'));

    ['/swagger', '/swagger.html'].forEach((path) => {
      this.app.route(path).get(controller.serveFile('swagger.html'));
    });

    this.app
      .route('/swagger-spec.json')
      .get(controller.serveFile('swagger-spec.json'));

    // GET requests
    this.app.route('/version').get(controller.version);

    this.app.route('/getpairs').get(controller.getPairs);
    this.app.route('/getnodes').get(controller.getNodes);
    this.app.route('/nodestats').get(controller.getNodeStats);
    this.app.route('/timeouts').get(controller.getTimeouts);
    this.app.route('/getcontracts').get(controller.getContracts);
    this.app.route('/getfeeestimation').get(controller.getFeeEstimation);

    // POST requests
    this.app.route('/routinghints').post(controller.routingHints);

    this.app.route('/swapstatus').post(controller.swapStatus);
    this.app.route('/swaprates').post(controller.swapRates);

    this.app.route('/gettransaction').post(controller.getTransaction);
    this.app.route('/getswaptransaction').post(controller.getSwapTransaction);
    this.app
      .route('/broadcasttransaction')
      .post(controller.broadcastTransaction);

    this.app.route('/createswap').post(controller.createSwap);
    this.app.route('/setinvoice').post(controller.setInvoice);

    this.app.route('/referrals/query').get(controller.queryReferrals);

    // EventSource streams
    this.app.route('/streamswapstatus').get(controller.streamSwapStatus);
  };
}

export default Api;
export { ApiConfig };
