# mega_sena_results_scraping
Get Mega sena results from http://loterias.caixa.gov.br/

####1.Install app/src/requirements.txt

####2: python app/src/migrations.py
will create all necessary directories 
- *log*: executions logs
- *raw*: files downloaded from Loterias Caixa
- *swamp*: where zip files are unziped 
- *lake*: transformed to treated csv format

###3: python app/src/[step].py [result_type]
to run each step

- step = [raw, swamp, lake]
- result_type = [megasena, quina, lotofacil]

###TO DO:
- orchestration of all steps
