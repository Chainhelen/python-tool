def getHeader(filename):
    file = open(filename);
    dict = {}
    while 1:
         line = file.readline().strip('\n');
         line = line.strip('\r');
         if not line:
             break;
         if line.find(':') != -1:
            li = line.split(':');
            dict[li[0]] =  li[1][1:];
    return dict
