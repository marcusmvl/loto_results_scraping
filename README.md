# mega_sena_results_scraping
Get Mega sena results from http://loterias.caixa.gov.br/

####1.Install app/src/requirements.txt

####2: run app/src/migrations.py
will create all necessary directories 
- **raw**: files downloaded from Loterias Caixa
- **swamp**: files unzip and transformed to csv format
- **log**: executions logs
- **temp**: where zip files are unziped

###3: run app/src/raw.py
to download Mega Sena results from Caixa (.zip format)

###4: run app/src/swamp.py
to unzip previous donwloaded file and transform in csv fixing rowspan "bug"