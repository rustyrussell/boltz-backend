import { getNestedObject } from './Utils';
import { satoshisToCoins } from '../DenominationConverter';
import StatsRepository, { StatsDate } from '../db/repositories/StatsRepository';

type MonthStats = {
  volume: Record<string, number>;
  trades: Record<string, number>;
  failureRates: {
    swaps: number;
    reverseSwaps: number;
  };
};

class Stats {
  public static generate = async (): Promise<
    Record<string, Record<string, MonthStats>>
  > => {
    const [volumes, tradeCounts, failureRates] = await Promise.all([
      StatsRepository.getVolume(),
      StatsRepository.getTradeCounts(),
      StatsRepository.getFailureRates(),
    ]);

    const stats = {};

    const getMonthObj = ({ year, month }: StatsDate) => {
      return getNestedObject(getNestedObject(stats, year), month);
    };

    volumes.forEach((volume) => {
      const obj = getNestedObject(getMonthObj(volume), 'volume');
      obj[volume.asset] = satoshisToCoins(volume.sum);
    });

    tradeCounts.forEach((counts) => {
      const obj = getNestedObject(getMonthObj(counts), 'trades');
      obj[counts.pair] = counts.count;
    });

    failureRates.forEach((fails) => {
      const obj = getNestedObject(getMonthObj(fails), 'failureRates');
      obj[fails.isReverse ? 'reverseSwaps' : 'swaps'] = fails.failureRate;
    });

    return stats;
  };
}

export default Stats;
