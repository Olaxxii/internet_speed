import speedtest
from datetime import datetime

def test_speed():
    print("Finding best server....")
    st=speedtest.Speedtest()
    st.get_best_server()

    print("Testing download.....")
    download=st.download()/1_000_000

    print("Testing upload.....")
    upload=st.upload()/1_000_000

    ping=st.results.ping

    print("\n" + "="*30)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Download: {download:.2f} Mbps")
    print(f"Upload: {upload:.2f} Mbps")
    print(f"Ping: {ping:.0f} ms")
    print("="*30)

    #Simple rating
    if download >= 50:
        print("Rating: EXCELLENT - 4K + gaming")
    elif download >= 15:
        print("Rating: GOOD - 1080p streaming")
    elif download>=5:
        print("Rating: FAIR - browsing ok")
    else:
        print("Rating: SLOW - check network")

if __name__ == "__main__":
    test_speed()