from funcoes import cria_json, backup


dicio = {'hex': '0x02114020', 'text':  'add $8, $16, $17'}
for contador in range(10):
    cria_json(dicio,contador)
backup()