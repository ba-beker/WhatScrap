import pywhatkit
import numpy as np

import requests
i = 0
while True:
    i+=1
    url = "LINK"

    headers = {
        "accept": "*/*",
        "accept-language": "fr",
        "authorization": "",
        "content-type": "application/json",
        "locale": "fr",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "x-app-version": "\"2.2.21\"",
        "x-referer": "https://www.ouedkniss.dz/boutiques",
        "x-track-id": "22c95e53-322f-4d88-9268-aaa015eff164",
        "x-track-timestamp": "1700919755",
    }

    payload = {
        "operationName": "SearchStore",
        "variables": {
            "q": "",
            "filter": {
                "categorySlug": "",
                "count": 12,
                "page": 1
            }
        },
        "query": """
            query SearchStore($q: String, $filter: StoreSearchFilterInput!) {
            stores: storeSearch(q: $q, filter: $filter) {
                data {
                id
                name
                slug
                description
                imageUrl
                followerCount
                announcementsCount
                url
                isVerified
                isOfficial
                mainLocation {
                    id
                    location {
                    id
                    region {
                        name
                        __typename
                    }
                    city {
                        name
                        __typename
                    }
                    __typename
                    }
                    __typename
                }
                announcements(count: 6, page: 1) {
                    data {
                    id
                    defaultMedia(size: SMALL) {
                        mediaUrl
                        __typename
                    }
                    __typename
                    }
                    __typename
                }
                __typename
                }
                paginatorInfo {
                lastPage
                __typename
                }
                __typename
            }
            }
        """,
    }

    response = requests.post(url, headers=headers, json=payload)
    ac = []
    print(response.status_code)
    for x in range(8):
        ac.append(response.json()["data"]["stores"]["data"][x]["announcementsCount"])
    id = response.json()["data"]["stores"]["data"][np.argmax(ac)]["id"]
    print("products :",np.max(ac))
    payload = {
        "operationName": "FetchByStore",
        "variables": {
            "id": id,
        },
        "query": """
            query FetchByStore($id: ID!) {
            siteBuild: siteBuildGetByStore(storeId: $id) {
                ...SiteBuildLayout
                __typename
            }
            }

            fragment SiteBuildLayout on SiteBuild {
            id
            createdAt
            publishedAt
            saved
            screenshotUrl
            theme {
                font
                dark
                color
                backgroundColor
                backgroundImg {
                full
                thumb
                __typename
                }
                __typename
            }
            pages {
                title {
                fr
                ar
                en
                __typename
                }
                type
                slug
                backgroundColor
                backgroundImg {
                full
                thumb
                __typename
                }
                visible
                blocks {
                type
                layout
                attrs
                __typename
                }
                __typename
            }
            headers {
                type
                layout
                attrs
                __typename
            }
            footers {
                type
                layout
                attrs
                __typename
            }
            queries {
                name {
                fr
                en
                ar
                __typename
                }
                q
                count
                filter
                cluster {
                name {
                    fr
                    en
                    ar
                    __typename
                }
                q
                count
                filter
                __typename
                }
                __typename
            }
            land {
                __typename
                ... on Market {
                id
                marketName: name
                descreption
                metakeywords
                logo
                __typename
                }
                ... on Store {
                id
                storeName: name
                slug
                description
                imageUrl
                iAmFollowing
                status
                categories {
                    id
                    name
                    slug
                    children {
                    id
                    name
                    slug
                    __typename
                    }
                    __typename
                }
                mainLocation {
                    id
                    worktime
                    phones
                    emails
                    faxes
                    socials {
                    name
                    url
                    __typename
                    }
                    location {
                    id
                    address
                    lat
                    lng
                    __typename
                    }
                    __typename
                }
                users {
                    user {
                    id
                    __typename
                    }
                    __typename
                }
                service {
                    params {
                    code
                    value
                    __typename
                    }
                    __typename
                }
                __typename
                }
            }
            __typename
            }
        """,
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)
    try :
        wname = response.json()["data"]["siteBuild"]["land"]["storeName"]
        wphone = response.json()["data"]["siteBuild"]["land"]["mainLocation"]["phones"][0]
        print(wphone)
        if not i % 2 :
            pywhatkit.sendwhatmsg_instantly(wphone,f"معايا {wname} ؟",wait_time=20,tab_close=True)
        if i % 2 :
            price = 4500
            scarcity = ""
            if i % 4 :
                pywhatkit.sendwhatmsg_instantly(wphone,f"""MESSAGE
        """,tab_close=True,wait_time=20)
            if not i % 4 :
                pywhatkit.sendwhatmsg_instantly(wphone,f"""Message""",tab_close=True,wait_time=20)
        if i % 2 :
            pywhatkit.sendwhats_image(wphone,"./img.jpg",tab_close=True,wait_time=20)
    except Exception as err :
        print(err)
    try :
        print(response.json()["data"]["siteBuild"]["land"]["mainLocation"]["emails"][0])
    except :
        pass
