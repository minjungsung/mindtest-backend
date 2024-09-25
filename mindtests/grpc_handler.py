from mindtests.pyproto import mindtest_pb2


def grpc_handler(message: mindtest_pb2.WebToServerRequest):
    global global_client_manager

    if message.HasField('get_questions'):
        return global_client_manager.get_questions(message.get_questions)
    elif message.HasField('submit_answers'):
        return global_client_manager.submit_answers(message.submit_answers)
    else:
        raise ValueError(f"Unsupported message type: {message}")