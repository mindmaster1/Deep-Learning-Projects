from subprocess import run,Popen,PIPE

cmd = ["dir"]
returncode = run(cmd)
# returncode是dir命令的退出状态码，通常来说, 一个为 0 的退出码表示进程运行正常
print(returncode)

with Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE,encoding="utf-8") as fs:
    fs.wait(2)

    files = fs.communicate()[0]
print(files)



