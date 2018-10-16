#coding:utf-8

import tarfile
import os
import subprocess
import time
import traceback
from multiprocessing import Process

def setup():
    cwd = os.path.dirname(os.path.realpath(__file__))
    exe = os.path.join(cwd, 'bin/nginx')
    if not os.path.exists(exe):
        with tarfile.open(os.path.join(cwd, 'nginx.tgz')) as t:
            t.extractall(cwd)

    try:
        subp = subprocess.Popen([exe, '-g', 'daemon off;'],
            cwd=cwd,
            env={"LD_LIBRARY_PATH": os.path.join(cwd, 'bin')})
        #subp.wait()
    except Exception:
        traceback.print_exc()


from sanic import Sanic
from sanic.response import text

app = Sanic()

@app.route("/")
async def test(request):
    return text('Hello World!')

if __name__ == "__main__":
    setup()
    app.run(host="127.0.0.1", port=8000)
