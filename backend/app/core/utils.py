from datetime import datetime, timezone

def	utcnow() -> datatime:
	"""UTC sem Timezone (O SQL n\ao guarda timezone)"""
	return (datetime.now(timezone.utc).replace(tzinfo=None))
