import time

#lambda or function that performs the API call
def retry_claude_call(call_function, max_retries=3, delay=2):

#claude response content as string, or None
    for attempt in range(1, max_retries + 1):
        try:
            return call_function()
        except Exception as e:
            print(f"[RetryHelper] Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                time.sleep(delay)
            else:
                print("[RetryHelper] All attempts failed.")
                return None