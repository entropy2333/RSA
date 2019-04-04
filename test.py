import RSA
import time
while True:
    m, d = RSA.main()
    doc = open('test.txt', 'a')
    print(m, d, file = doc)
    doc.close()
    time.sleep(1)