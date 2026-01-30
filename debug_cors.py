import requests

TARGET_URL = "https://backend-car-wash.vercel.app/api/memberships"
ORIGIN = "https://frontend-car-wash.vercel.app"

print(f"📡 Testing OPTIONS request to: {TARGET_URL}")
print(f"   Origin: {ORIGIN}")

try:
    response = requests.options(
        TARGET_URL,
        headers={
            "Origin": ORIGIN,
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "authorization"
        },
        timeout=10
    )
    
    print("\n✅ Response Status:", response.status_code)
    print("📋 Headers:")
    for k, v in response.headers.items():
        if "access-control" in k.lower():
            print(f"  - {k}: {v}")
            
    if "Access-Control-Allow-Origin" not in response.headers:
        print("\n❌ CORS Header MISSING in OPTIONS response!")
    else:
        print("\n✅ CORS Headers present.")

except Exception as e:
    print(f"\n❌ Request Failed: {e}")

print("\n" + "="*40 + "\n")
print(f"📡 Testing GET request (No Auth) to: {TARGET_URL}")
try:
    response = requests.get(
        TARGET_URL,
        headers={"Origin": ORIGIN},
        timeout=10
    )
    print(f"✅ Status: {response.status_code}")
    print(f"📋 Body prefix: {response.text[:100]}")
except Exception as e:
    print(f"❌ GET Failed: {e}")
