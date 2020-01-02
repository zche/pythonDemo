module_path = "BertVectorsFeaturizer"
module_path = "CRFEntityExtractor"
CRFEntityExtractor = "对方水电费"
str1 = "dsfds"
print(str1)
module1 = globals()["CRFEntityExtractor"]
local1 = locals()["CRFEntityExtractor"] 
module = globals().get(module_path, locals().get(module_path))
print(module)
modules = globals()
print("以下是globals：")
print(modules) 

localsVari = locals()
print("以下是local：")
print(locals)