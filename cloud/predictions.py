from google.cloud import aiplatform


def get_imdb_sentiment(proejct_id,location,endpoint_id,instances):
    result="****Cloud predicition****\n"

    aiplatform.init(project=proejct_id,location=location)
    point=aiplatform.Endpoint(endpoint_id)

    if isinstance(instances,list):
        preds=point.predict(instances=instances).predictions[0]

        for k,v in preds.items():
            result+=f"{k} : {v}\n"

        return result
    else:
        return f"Input type error:{type(instances)}"


