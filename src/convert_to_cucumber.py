import json
import behave2cucumber
import os

# O pacote Allure para geração de relatórios com behave está indisponível nos repositórios online,
# com a biblioteca atual behave 2 cucumber pretendia gerar os relatórios após a conversão dos arquvios Json
# não foi possível, houve problemas na instalação do pacote behave2cucumber e problemas na execução do script de conversão

for filename in os.listdir("/home/brenobaiardi/AME-Python/report"):

    with open("/home/brenobaiardi/AME-Python/report/" + filename) as behave_json:
        cucumber_json = behave2cucumber.convert(json.load(behave_json))
        outputfile = open(
            "/home/brenobaiardi/AME-Python/reportcucumber/"+filename, mode="w+")
        outputfile.write(cucumber_json)
