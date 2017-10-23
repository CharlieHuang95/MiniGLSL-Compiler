import os

if __name__=="__main__":
    for f in os.listdir("parser_test_cases"):
        os.system("compiler467 -Tp < parser_test_cases/" + f + " > parser_test_cases/test_output/" + f + ".out")
        if f.startswith("fail"):
            print f
