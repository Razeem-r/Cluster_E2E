import sys
from src.logger import logging

def error_msg_detail(error , error_deet):
    _,_,exc_tb = error_deet.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f'Error occured in python file name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]'
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_msg,error_deet:sys):
        super().__init__(error_msg)
        self.error  = error_msg_detail(error_msg,error_deet = error_deet)

    def __str__(self) -> str:
        return self.error
    
