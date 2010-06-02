status = dict(
    bills=True,
    bill_versions=True,
    sponsors=True,
    actions=True,
    votes=True,
    legislators=True,
    contributors=['Jeremy Carbaugh', 'James Turk'],
    notes="",
)

from fiftystates.scrape.md.bills import SESSIONS

metadata = dict(
    state_name='Vermont',
    legislature_name='Maryland General Assembly',
    upper_chamber_name='Senate',
    lower_chamber_name='House of Delegates',
    upper_title='Senator',
    lower_title='Delegate',
    upper_term=4,
    lower_term=4,
    sessions=SESSIONS.keys(),
    session_details={}
)
