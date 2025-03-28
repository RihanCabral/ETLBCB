from etlBCB.src.extractTransform import requestApiBcb

dadosBcb = requestApiBcb('20191')
print(dadosBcb)