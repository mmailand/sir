def top_prefixes(g, request):
    # curl http://127.0.0.1:5000/api/v1.0/top_prefixes\?limit_prefixes=10\&start_time\=2015-07-13T14:00\&end_time\=2015-07-14T14:00
    db = getattr(g, 'db')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    limit_prefixes = int(request.args.get('limit_prefixes', 0))
    net_masks = request.args.get('net_masks', '')
    exclude_net_masks = request.args.get('exclude_net_masks', False)

    data = {
        'result': {
            'top_prefixes': db.aggregate_per_prefix(
                start_time, end_time,
                limit=limit_prefixes,
                net_masks=net_masks,
                exclude_net_masks=exclude_net_masks),
        },
        'parameters': {
            'limit_prefixes': limit_prefixes,
            'start_time': start_time,
            'end_time': end_time,
            'net_masks': net_masks,
            'exclude_net_masks': exclude_net_masks,
        },
        'meta': {
            'request_time': getattr(g, 'request_time')(),
        },
    }
    return data


def top_asns(g, request):
    # curl http://127.0.0.1:5000/api/v1.0/top_asns\?start_time=2015-07-13T14:00\&end_time=2015-07-14T14:00
    db = getattr(g, 'db')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    data = {
        'result': {
            'top_asns': db.aggregate_per_as(start_time, end_time),
        },
        'parameters': {
            'start_time': start_time,
            'end_time': end_time,
        },
        'meta': {
            'request_time': getattr(g, 'request_time')(),
        },
    }
    return data
