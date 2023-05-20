import psutil
import datetime

class SystemData:

    @staticmethod
    def get_sys_data() -> dict:
        output = {}
        cpu = SystemData.get_cpu_times()
        mem = SystemData.get_virtual_memory()
        pids = SystemData.get_pid_count()

        output.update(cpu)
        output.update(mem)
        output['pid_count'] = pids
        output['timestamp'] = datetime.datetime.now().timestamp()

        return output
        
    @staticmethod
    def get_cpu_times() -> dict:
        cpu_response = psutil.cpu_times()
        user_time = cpu_response.user
        system_time = cpu_response.system
        idle_time = cpu_response.idle
        return {
            "user_time":  user_time,
            "system_time": system_time,
            "idle_time": idle_time
        }

    @staticmethod
    def get_virtual_memory() -> dict:
        memory_response = psutil.virtual_memory()
        avail_memory = memory_response.available
        used_memory = memory_response.used
        return {
            "avail_memory": avail_memory,
            "used_memory": used_memory
        }

    @staticmethod
    def get_pid_count() -> int:
        pids = psutil.pids()
        num_pids = len(pids)
        return num_pids
    
    @staticmethod
    def add_tenant_name(data, tenant_name) -> dict:
        data['tenant'] = tenant_name
        return data
    
    