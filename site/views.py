from billy import db

from django.shortcuts import render_to_response, redirect

def detailed_status(request):
    states = []
    for meta in list(db.metadata.find()):
        state = {}
        state['id'] = meta['_id']
        s_spec = {'state': state['id']}
        state['name'] = meta['name']
        counts = db.counts.find_one({'_id': state['id']})
        if counts:
            counts = counts['value']
            state['bills'] = counts['bills']
            state['votes'] = counts['votes']
            state['legislators'] = db.legislators.find(s_spec).count()
            state['committees'] = db.committees.find(s_spec).count()
            state['events'] = db.events.find(s_spec).count()
            state['subjects'] = counts['subjects'] > 1
            #active_legs = db.legislators.find({'state': state['id'],
            #                                   'active': True}).count()

        states.append(state)

    states.sort(key=lambda x: x['id'] if x['id'] != 'total' else 'zz')

    return render_to_response('detailed_status.html', {'states': states})


def downloads(request):
    states = sorted(db.metadata.find(), key=lambda x:x['_id'])
    return render_to_response('downloads.html', {'states':states})


def data_zip(request, state):
    metadata = db.metadata.find_one({'_id': state})
    if not metadata or 'latest_dump_url' not in metadata:
        raise Http404
    return redirect(metadata['latest_dump_url'])
