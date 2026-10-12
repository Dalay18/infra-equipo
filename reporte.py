import ctypes
import os
import platform
import shutil
import socket
from datetime import datetime


def memoria():
    class MEMORYSTATUSEX(ctypes.Structure):
        _fields_ = [
            ("dwLength", ctypes.c_ulong),
            ("dwMemoryLoad", ctypes.c_ulong),
            ("ullTotalPhys", ctypes.c_ulonglong),
            ("ullAvailPhys", ctypes.c_ulonglong),
            ("ullTotalPageFile", ctypes.c_ulonglong),
            ("ullAvailPageFile", ctypes.c_ulonglong),
            ("ullTotalVirtual", ctypes.c_ulonglong),
            ("ullAvailVirtual", ctypes.c_ulonglong),
            ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
        ]
    est = MEMORYSTATUSEX()
    est.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(est))
    return est.ullTotalPhys / 1024**2, est.ullAvailPhys / 1024**2


def main():
    total, usado, libre = shutil.disk_usage("C:\\")
    mem_total, mem_disp = memoria()

    lineas = [
        f"Reporte generado: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Equipo: {socket.gethostname()}",
        f"Sistema: {platform.system()} {platform.release()}",
        f"Procesadores: {os.cpu_count()}",
        f"Disco C:\\ {usado / 1e9:.1f} GB usados de {total / 1e9:.1f} GB",
        f"Memoria: {mem_disp:.0f} MB disponibles de {mem_total:.0f} MB",
    ]

    carpeta = os.path.join(os.path.expanduser("~"), "automatizacion")
    os.makedirs(carpeta, exist_ok=True)
    with open(os.path.join(carpeta, "reporte.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lineas) + "\n")
    print("\n".join(lineas))


if __name__ == "__main__":
    main()
