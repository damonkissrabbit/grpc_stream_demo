if __name__ == '__main__':
    import os
    os.system(
        "python "
        "-m grpc_tools.protoc "
        "--proto_path=. "
        "--python_out=. "
        "--grpc_python_out=.  "
        "./calculator.proto")
