# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hold.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\nhold.proto\x12\x04hold"\x10\n\x0eGetInfoRequest""\n\x0fGetInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t"\xed\x01\n\x0eInvoiceRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\x12\x13\n\x0b\x61mount_msat\x18\x02 \x01(\x04\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06\x65xpiry\x18\x04 \x01(\x04H\x01\x88\x01\x01\x12"\n\x15min_final_cltv_expiry\x18\x05 \x01(\x04H\x02\x88\x01\x01\x12(\n\rrouting_hints\x18\x06 \x03(\x0b\x32\x11.hold.RoutingHintB\x0e\n\x0c_descriptionB\t\n\x07_expiryB\x18\n\x16_min_final_cltv_expiry"!\n\x0fInvoiceResponse\x12\x0e\n\x06\x62olt11\x18\x01 \x01(\t"#\n\x13RoutingHintsRequest\x12\x0c\n\x04node\x18\x01 \x01(\t"q\n\x03Hop\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x18\n\x10short_channel_id\x18\x02 \x01(\t\x12\x10\n\x08\x62\x61se_fee\x18\x03 \x01(\x04\x12\x0f\n\x07ppm_fee\x18\x04 \x01(\x04\x12\x19\n\x11\x63ltv_expiry_delta\x18\x05 \x01(\x04"&\n\x0bRoutingHint\x12\x17\n\x04hops\x18\x01 \x03(\x0b\x32\t.hold.Hop"8\n\x14RoutingHintsResponse\x12 \n\x05hints\x18\x01 \x03(\x0b\x32\x11.hold.RoutingHint"9\n\x0bListRequest\x12\x19\n\x0cpayment_hash\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0f\n\r_payment_hash"H\n\x04Htlc\x12\x1e\n\x05state\x18\x01 \x01(\x0e\x32\x0f.hold.HtlcState\x12\x0c\n\x04msat\x18\x02 \x01(\x04\x12\x12\n\ncreated_at\x18\x03 \x01(\x04"\xb5\x01\n\x07Invoice\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\x12\x1d\n\x10payment_preimage\x18\x02 \x01(\tH\x00\x88\x01\x01\x12!\n\x05state\x18\x03 \x01(\x0e\x32\x12.hold.InvoiceState\x12\x0e\n\x06\x62olt11\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\x04\x12\x19\n\x05htlcs\x18\x06 \x03(\x0b\x32\n.hold.HtlcB\x13\n\x11_payment_preimage"/\n\x0cListResponse\x12\x1f\n\x08invoices\x18\x01 \x03(\x0b\x32\r.hold.Invoice")\n\rSettleRequest\x12\x18\n\x10payment_preimage\x18\x01 \x01(\t"\x10\n\x0eSettleResponse"%\n\rCancelRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t"\x10\n\x0e\x43\x61ncelResponse"$\n\x0cTrackRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t"2\n\rTrackResponse\x12!\n\x05state\x18\x01 \x01(\x0e\x32\x12.hold.InvoiceState"\x11\n\x0fTrackAllRequest"[\n\x10TrackAllResponse\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\x12\x0e\n\x06\x62olt11\x18\x02 \x01(\t\x12!\n\x05state\x18\x03 \x01(\x0e\x32\x12.hold.InvoiceState*a\n\x0cInvoiceState\x12\x12\n\x0eINVOICE_UNPAID\x10\x00\x12\x14\n\x10INVOICE_ACCEPTED\x10\x01\x12\x10\n\x0cINVOICE_PAID\x10\x02\x12\x15\n\x11INVOICE_CANCELLED\x10\x03*D\n\tHtlcState\x12\x11\n\rHTLC_ACCEPTED\x10\x00\x12\x10\n\x0cHTLC_SETTLED\x10\x01\x12\x12\n\x0eHTLC_CANCELLED\x10\x02\x32\xd7\x03\n\x04Hold\x12\x38\n\x07GetInfo\x12\x14.hold.GetInfoRequest\x1a\x15.hold.GetInfoResponse"\x00\x12\x38\n\x07Invoice\x12\x14.hold.InvoiceRequest\x1a\x15.hold.InvoiceResponse"\x00\x12G\n\x0cRoutingHints\x12\x19.hold.RoutingHintsRequest\x1a\x1a.hold.RoutingHintsResponse"\x00\x12/\n\x04List\x12\x11.hold.ListRequest\x1a\x12.hold.ListResponse"\x00\x12\x35\n\x06Settle\x12\x13.hold.SettleRequest\x1a\x14.hold.SettleResponse"\x00\x12\x35\n\x06\x43\x61ncel\x12\x13.hold.CancelRequest\x1a\x14.hold.CancelResponse"\x00\x12\x34\n\x05Track\x12\x12.hold.TrackRequest\x1a\x13.hold.TrackResponse"\x00\x30\x01\x12=\n\x08TrackAll\x12\x15.hold.TrackAllRequest\x1a\x16.hold.TrackAllResponse"\x00\x30\x01\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "hold_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_INVOICESTATE"]._serialized_start = 1285
    _globals["_INVOICESTATE"]._serialized_end = 1382
    _globals["_HTLCSTATE"]._serialized_start = 1384
    _globals["_HTLCSTATE"]._serialized_end = 1452
    _globals["_GETINFOREQUEST"]._serialized_start = 20
    _globals["_GETINFOREQUEST"]._serialized_end = 36
    _globals["_GETINFORESPONSE"]._serialized_start = 38
    _globals["_GETINFORESPONSE"]._serialized_end = 72
    _globals["_INVOICEREQUEST"]._serialized_start = 75
    _globals["_INVOICEREQUEST"]._serialized_end = 312
    _globals["_INVOICERESPONSE"]._serialized_start = 314
    _globals["_INVOICERESPONSE"]._serialized_end = 347
    _globals["_ROUTINGHINTSREQUEST"]._serialized_start = 349
    _globals["_ROUTINGHINTSREQUEST"]._serialized_end = 384
    _globals["_HOP"]._serialized_start = 386
    _globals["_HOP"]._serialized_end = 499
    _globals["_ROUTINGHINT"]._serialized_start = 501
    _globals["_ROUTINGHINT"]._serialized_end = 539
    _globals["_ROUTINGHINTSRESPONSE"]._serialized_start = 541
    _globals["_ROUTINGHINTSRESPONSE"]._serialized_end = 597
    _globals["_LISTREQUEST"]._serialized_start = 599
    _globals["_LISTREQUEST"]._serialized_end = 656
    _globals["_HTLC"]._serialized_start = 658
    _globals["_HTLC"]._serialized_end = 730
    _globals["_INVOICE"]._serialized_start = 733
    _globals["_INVOICE"]._serialized_end = 914
    _globals["_LISTRESPONSE"]._serialized_start = 916
    _globals["_LISTRESPONSE"]._serialized_end = 963
    _globals["_SETTLEREQUEST"]._serialized_start = 965
    _globals["_SETTLEREQUEST"]._serialized_end = 1006
    _globals["_SETTLERESPONSE"]._serialized_start = 1008
    _globals["_SETTLERESPONSE"]._serialized_end = 1024
    _globals["_CANCELREQUEST"]._serialized_start = 1026
    _globals["_CANCELREQUEST"]._serialized_end = 1063
    _globals["_CANCELRESPONSE"]._serialized_start = 1065
    _globals["_CANCELRESPONSE"]._serialized_end = 1081
    _globals["_TRACKREQUEST"]._serialized_start = 1083
    _globals["_TRACKREQUEST"]._serialized_end = 1119
    _globals["_TRACKRESPONSE"]._serialized_start = 1121
    _globals["_TRACKRESPONSE"]._serialized_end = 1171
    _globals["_TRACKALLREQUEST"]._serialized_start = 1173
    _globals["_TRACKALLREQUEST"]._serialized_end = 1190
    _globals["_TRACKALLRESPONSE"]._serialized_start = 1192
    _globals["_TRACKALLRESPONSE"]._serialized_end = 1283
    _globals["_HOLD"]._serialized_start = 1455
    _globals["_HOLD"]._serialized_end = 1926
# @@protoc_insertion_point(module_scope)
