import requests
import index

username = index.username
password = index.password
token = 'P0_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiZE9OU1FqZUswTExIUGw2bENacTVRRHhvNlJ4QlNnbUlYeTdSV2Mzbi9ZWTJLZ0gvR3puTjlHbnhKZWR3ZTBjc3JFbWNtUFhlVENwM2ducXBLejVpd0tsVmtRMnI2ZDZVN2NOVXRIUGcrc25zSEJvZFl0WTBZVDNFV09oYVFWYzVkUnMyTUNSYzVGMTQrUXMzZXVIQllEVFpsZXBkcXFnTndPRWdSZTExU1ZqNnExdHlZaXFRTnRFVkIyOThUVnBGK212dHBJSFFLSkJxL3pqY2E5ZytKV0liMHpyeUZYMGV4UFptTTQ5Ry9aWVNsODR0ZlhNUWxYb2ZZa2tDZmVPczdHWEk5VTF1SytqVzRnRk1CcE1pQXg4SjVYZHc4a21ycjRrbjJZd3gxQXAxUHJDdWJjSU1nVkF3M2NVdmVrWXBRYmRoVkNVdi8vaTlBcnh1aFJYRVFYQVdqZGFwK2tPMlVEbDltZVo3RHhZeks4b0pxbXgvcE1uWEV6T3BWRVAvMERKdHR6dlhJRFd0TXBWbjVVU2R3QzJ4Vk01ZUFEbndQNXI2WitHWEtHQ05RTTNhT0JRV3UyOFRDSURUak5uUHozMmw5ZHFkanVzWUZENWIvVkRId2U4M3JMbll6MU11VjlnQys2cDdvdzdFOHAySkhjVUpZUmIvYVlxaVkvSjJ1VG9MeWxrenMrSSt4VUQrNDZrMUFHemUxS1Y0QzUyQzkyQTc0MXZ0eUJzMzJ0M2FLN1ZTcDBQVmhiZFNjVG1Eb3ZUTFFpcENJNXRTMTd1ajEwaXowbnJ3anptU0pmTmoveGp6NWxhc2FXWHpuWGthMU82TE8zbFlqQ3dhYmViTnp2cS9KU1ZQR3hmWE9YQjQrYVQrbFd0OVd4MlNoOUprRVl0OC8yUHlvb1ZVTWZTRlpEUWtaN05LL0dHbi9jMzZOd3NyNjUvd0tjMFBPdkdERTVTSHBWVmpyUTluVlM4VGhJU0c4aTNoSlFqZnJ0aklGMWNzb2tPdVplbUhUa05UM05vRXordkdWdWVVVzd0SlQxQlZVZG5RTlVLd2tLVnpCdEl0YjNuQVpIdFFFTWJCbHBWZEhYQURHVnR4UnpSVk1lN1AvK0NJU3hhb1VvUnk3VGJMYkJKczZISzdXTitGMDV2djFuZDNTclFXVVBWOFNtK004bEVWUEZRZ0J4NEtZbXFocHNZaUZUK21LZmVMUTROdlJ4K2g1UlF2YS9iOTZnWW4yVWVka1NGUEYrUytTWW9IZ1FDTVc2M1VDVVZpRnZ6TXc1SXNROFU5NHRXVHpERmE4WmswVnhqZDVWaXZ6eUpiaHREbzh5ekoyNVU4Vk9pZDhaZkpJY2svY25pOFBZaG80UWdqQ290V0xOQ2lQVWhsTTl2ejhpbXdQSUpYRnVWaThOc09rNG1qQVNwV05qNE93Tm9nSnJkVnAvOFBUcHhpUWVWZ0dOY2d1QkFuZVpzelRVRzMwTnJPK1lFWDFib2c5cUxwemRMUEhacWRjSi82bzVzMmlSb1RnVTc1dGt0OXpkblFqUFhiU0JOQkNRWDlWRlE1NGNYejl3R3gxK3BkOUJCSUN6TU4zemRQVkRzMWJDTU5rdGl6NVVtdXlPZDVqQTJhWlhwY0hhQk51bnFYZ2wyVU9xbGh6dkJOTzl0SmNCaVhYaFFKbHY4WkhINXFOS005dDhqcHdSRGw0UnBsOXJjS1g0bGFMNjZMcGNDeFhQU3pHZ2pSYWkwcWJzVWVWdXlIdGtKUGNxSkdha0hrUnJLT0IvWjYreW9sOUxJRlplWGlQTkFzM3pVd2pYNllRakRHbW4yOFRicjZ6ZG1vRENnQ3V4QzNzUG1pVXkzL0FFQzA1MXRwRnVtMjVMMDNiUHFQeDB2eThzR0UxUldDeGFrZGRNVTkxRm4rN1EwRWx0eS9QWEN0YlFoVWZmRG5NWnhtTjVVZjI5eDl4SlBFNnI4V0tyckRTUklPZkRPaFJiTVc5aVl0bm1MWmdyT2FKK2VkNFpKUUR4WFhLWkhSd0w1QjBTQnpVZDFybXNJS2pEcUY1ajl3dEdCaERmOGlSaFVlVXp2emZwajk3emJwQ2hCYmcxbHBNRUh3bnc9PW1zby9MZFhOUmhObmhaUEsiLCJleHAiOjE2NjM1MDc3MTIsInNoYXJkX2lkIjozMzk1MTAzMDMsInBkIjowfQ.l69w2mHDPD2IFX4aHWie2SHy52PAcl0J82ObV_UWyT4'
cookies1 = 'ref=start; cid=82674870; remember_optout=0; PHPSESSID=72uur3ptaod5gjklbokkvpdved8ccrg3g9htp5gu1faner0n'
useragent1 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'



authurl = 'https://www.die-staemme.de/page/auth'

url = 'https://www.die-staemme.de/'

s = requests.session()
s.headers

res = s.get(url)

data = f"username={username}&password={password}&remember=1&token={token}"

res = s.post(authurl, data, allow_redirects=False, cookies = cookies1)

print(res)
#print(res.text)









