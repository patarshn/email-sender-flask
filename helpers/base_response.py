from flask import jsonify

def baseResponseSuccess(data, message = "Success get data"):
    res = {
        "data" : data,
        "message" : message,
        "error" : False
    }
    return jsonify(res), 200

def baseResponseSuccessCreated(data, message = "Success create data"):
    res = {
        "data" : data,
        "message" : message,
        "error" : False
    }
    return jsonify(res), 200

def baseResponseErrorNotFound(message = "Data Not Found"):
    res = {
        "data" : None,
        "message" : message,
        "error" : True
    }
    return jsonify(res), 404

def baseResponseError(data, message):
    res = {
        "data" : data,
        "message" : message,
        "error" : True
    }
    return jsonify(res), 500