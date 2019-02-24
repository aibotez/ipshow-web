from django.shortcuts import render
import time
def home(request):
    tim = time.strftime('%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))


    with open(r'F:\py项目\代理\httpslist-1.txt','r') as f:
        ips = f.read()
    ip = ips.split()
    with open(r'F:\py项目\代理\httplist-1.txt','r') as f:
        ipp = f.read()
    ipp = ipp.split()
    ds = {'s':ip,'p':ipp,'user_info':[],'time':tim}
    res = request.META
    ds['user_info'].append('你的IP '+res['HTTP_X_REAL_IP'])
    #ds['user_info'].append(res['HTTP_USER_AGENT'])
    print('新用户')
    root_info0 = res['HTTP_USER_AGENT']
    print(root_info0)

    root_info = root_info0.split(' ')

    root_info_xi=''
    root_info_p=''



    root_info_xi=root_info0.split(' ')[1]
    print(root_info_xi)
    if root_info_xi =='(Windows':
        root_info_xi = 'Windows'+'( NT'+root_info[3]+' )'
    else:
        root_info1 = root_info0.split(';')
        if len(root_info1[1])>3:
            root_info_xi = root_info1[1]
        else:
            root_info_xi=root_info1[2]
        root_info1 = root_info0.split('(')[1]
        root_info1 = root_info1.split(')')[0]
        root_info1 = root_info1.split(';')
        if len(root_info1[-1])>8:
            root_info_p = root_info1[-1]
        else:
            root_info_p = root_info1[-2]
    if root_info_p == '':
        root_info_p='电脑'
    ds['user_info'].append('你的系统 '+ root_info_xi)
    ds['user_info'].append('你的机子 ' + root_info_p)

    net = root_info0.split(' ')
    for s in net:
        net1 = s.split('/')
        if net1[0] =='NetType':
            ds['user_info'].append('网络状态： '+net1[1])

    #print(root_info_xi,root_info_p)
    with open('123.txt','a+')as f:
        tim = time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))
        f.write(tim)
        f.write('\n')
        for s in ds['user_info']:
            f.write(s)
            f.write('\t')
        f.write('\n\n')

    print(ds['user_info'])

    return  render(request,'home.html',ds)