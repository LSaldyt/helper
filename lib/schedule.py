import datetime, time
from pprint import pprint
from lib import get_service, get_events

def get_time(event, loc):
    s = event[loc].get('dateTime', event[loc].get('date'))
    return s

def get_hour(event, loc):
    s = get_time(event, loc)
    day = s[:10]
    time = s[11:-6]
    return datetime.datetime.strptime(day + ' ' + time, '%Y-%m-%d %X')

def duration(event):
    return abs((get_hour(event, 'end') - get_hour(event, 'start')).total_seconds() / 60)

def get_schedule(n=20):
    schedule = []

    service = get_service()
    events  = get_events(service, n=20)

    if len(events) > 0:
        first = events[0]
        schedule.append((duration(first), first['summary']))

        now = datetime.datetime.strptime(
                time.strftime('%Y-%m-%d %X'),
                '%Y-%m-%d %X')

        gap = get_hour(first, 'start') - now
        minutes = gap.total_seconds() / 60
        schedule.append((minutes, 'gap'))

    for a, b in zip(events[:-1], events[1:]):
        aEnd   = get_hour(a, 'end')
        bStart = get_hour(b, 'start')
        gap = bStart - aEnd
        minutes = gap.total_seconds() / 60

        schedule.append((duration(a), a['summary']))
        schedule.append((minutes, 'gap'))

    if len(events) > 1:
        last = events[-1]
        schedule.append((duration(last), last['summary']))

    return schedule

#def main():
#    service = get_service()
#    events = get_events(service, n=20)
#
#    if not events:
#        print('No upcoming events found.')
#    for event in events:
#        start = get_time(event, 'start')
#        print(start, event['summary'])
#
#    if len(events) > 0:
#        first = events[0]
#        now = datetime.datetime.strptime(time.strftime('%X'), '%X')
#        gap = get_hour(first, 'start') - now
#        print('Gap until: ', first['summary'])
#        print('{} minutes'.format(gap.total_seconds() / 60))
#
#    for a, b in zip(events[:-1], events[1:]):
#        aEnd   = get_hour(a, 'end')
#        bStart = get_hour(b, 'start')
#        gap = bStart - aEnd
#
#        print('Gap after: ', a['summary'])
#        print('{} minutes'.format(gap.total_seconds() / 60))
#
#    pprint(get_schedule())
#
#    #events = create_event(service)
#    #print(events)
#
#if __name__ == '__main__':
#    main()

