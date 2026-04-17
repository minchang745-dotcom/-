import os
from supabase import create_client
from datetime import datetime, timedelta
import requests

def main():
    # 1. Supabase 연결 (깃허브 비밀금고에서 정보를 가져옵니다)
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)

    # 2. 내일 날짜 계산 (KST 한국 시간 기준)
    # 깃허브 서버는 UTC 기준이므로 +9시간을 고려해야 하지만, 단순화를 위해 날짜만 계산합니다.
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    print(f"조회 날짜: {tomorrow}")

    # 3. 내일 일정이 있는 데이터 가져오기
    response = supabase.table("user_events").select("*").eq("event_date", tomorrow).execute()
    events = response.data

    if not events:
        print("내일 일정이 있는 사용자가 없습니다.")
        return

    for event in events:
        user_id = event['user_id']
        event_name = event['event_name']
        
        # 4. 알림 전송 (지금은 테스트를 위해 프린트만 합니다)
        print(f"알림 전송 대상: {user_id} / 일정: {event_name}")
        
        # [추후 여기에 카카오톡 전송 API 코드가 들어갑니다]

if __name__ == "__main__":
    main()
