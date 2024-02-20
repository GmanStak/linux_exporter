import argparse, json
from configparser import RawConfigParser

def main(args):
    print("--address {0}".format(args.code_address))  # args.address会报错，因为指定了dest的值
    print("--flag {0}".format(args.flag))  # 如果命令行中该参数输入的值不在choices列表中，则报错
    print("--port {0}".format(args.port))  # prot的类型为int类型，如果命令行中没有输入该选项则报错
    print("-l {0}".format(args.log))  # 如果命令行中输入该参数，则该值为True。因为为短格式"-l"指定了别名"--log"，所以程序中用args.log来访问


def get_config(config_path):
    config = RawConfigParser()
    config.read(config_path, encoding='UTF8')
    host = config.get('default', "host")
    port = config.get('default', "port")
    username = config.get('default', "username")
    password = config.get('default', "password")
    # 当配置文件包含列表，字典等，需要使用json.loads去掉括号
    h_list = config.get('default', "host_list")
    host_list = json.loads(h_list)
    return host, port, username, password, host_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
    # parser.add_argument("--address", default=80, help="the port number.", dest="code_address")
    parser.add_argument("--address", help="the port number.", dest="code_address")
    parser.add_argument("--flag", choices=['.txt', '.jpg', '.xml', '.png'], default=".txt", help="the file type")
    parser.add_argument("--port", type=int, required=True, help="the port number.")
    parser.add_argument("-l", "--log", default=False, action="store_true", help="active log info.")

    args = parser.parse_args()
    main(args)
