from flask import Flask, jsonify
from tasks import count_file
app = Flask(__name__)

WORDS  = ["han","hon","hen","den","det","denne","denna"]
FILES =[
"05cb5036-2170-401b-947d-68f9191b21c6",  "7a27e92f-82dd-4482-8edd-2296dde80fcd",
"094b1612-1832-429e-98c1-ae06e56d88d6",  "7c9ca018-21e0-47e9-8028-47d72d7e09f5",
"0c7526e6-ce8c-4e59-884c-5a15bbca5eb3",  "8241f565-05f7-45bc-a034-1b524b355ff5",
"0d7c752e-d2a6-474b-aef4-afe5dc506e33",  "82bce29e-18ec-4c35-9038-57f74af32907",
"0ecdf8e0-bc1a-4fb3-a015-9b8dc563a92f",  "83cab067-bb23-4ea0-80c9-785aa611237a",
"12b53361-29e8-411e-be18-f879564ca94b",  "8474d838-31d6-43e4-a437-282612c3fd53",
"154e5847-81a5-49de-9eac-45a91d3fb8d1",  "8652018f-cfd4-4dab-b8f3-f51092b2e9f7",
"16f04130-aa4a-4534-be0a-eaf314dc88f3",  "88b8526c-84b7-4b5a-bb6f-e12d0be4667d",
"1e73ea44-9842-4aa3-b043-603ad3edcc1d",  "89372688-4331-4053-98bd-74f8d0bf08da",
"1e7f83b2-5b3f-47b7-976b-d5e6f2d93f1b",  "8da2fbba-a8f5-4a38-a25c-3339b2bed2cf",
"20275995-d9e1-442c-bf33-7979aab6db8b",  "8e1eed1c-277f-4b10-8788-1ab8c371b1fb",
"205d09fc-3916-4b90-8ed2-6c908186011a",  "8fb8a27b-18fd-4ffe-8f56-3b808cb66cd7",
"2082ad71-ea40-4f34-a5d8-df001f49f770",  "90ddac10-7b61-4ecc-9a11-77eecdbb6baf",
"254e0714-d659-40fd-80ce-34864144252c",  "92586054-e548-42a0-b1c0-610c1b5d72ee",
"270cc06b-97d4-4f38-8512-81a4616cfc9a",  "9607f4ca-dbf1-47bb-b244-b08b22f2b46e",
"2714028c-9830-43a9-baa7-8f9b4055c7cb",  "9988f78b-cf0b-4317-a76f-811b6269075b",
"298d4b64-1dfe-428a-a644-5164780993bc",  "9b9a314e-34d0-4552-a903-01b40c6076a1",
"29c2d795-c414-490e-9e54-54641705f542",  "9e76f0e7-562c-4a1e-af0a-33533ed6f79f",
"2c359499-d31d-4f39-b9d4-9a71b68bf995",  "9f19afc2-d6d2-47b1-801e-32165e14f3e1",
"2c4d5fa5-0495-4a19-8567-ca1d17dd15b0",  "9fd91867-e0b8-4465-a223-85e8df6feae2",
"2c4ee64d-d125-4a9f-9962-1acf4e0ad264",  "a0108473-09a9-4415-ba3c-be10a40ad109",
"2cba3957-bbc1-441c-89b5-7b07590103d8",  "a0964e3b-66a2-424f-bd18-d35ff31d2efb",
"2d2e0831-4a66-4294-8984-6c1fd70abff3",  "a5168e9b-72a1-4d6a-825b-8fa603e38cf6",
"2ebe6321-dafc-46e8-a10a-d934608edde3",  "a9849af5-4bd4-4488-b006-c5d3cb1e863e",
"332a01e3-f9f7-4d5f-bc9c-19a6263cb620",  "aba4d2b8-a5df-4405-908d-e6f7c62897d2",
"3c0e60ce-1f50-496a-8335-7a118f50843c",  "b694c069-9c5e-4f44-b5b2-48fc8c976370",
"3e5fe85a-5756-432f-b5c7-939128ca16d6",  "bb40ffc6-6f5e-48c9-bdd4-0f065dee9bf3",
"42abd525-33a5-4c77-8155-ff0382cd9209",  "bf96ea63-74ad-49d7-80ae-6f6ac9c6a71a",
"46d1c1ea-f1d7-4963-a56e-440d868bee10",  "c14f5b82-f918-4313-978d-907e639b0bf6",
"47a8d5b1-95c5-430b-918b-033e91351e43",  "c17107b2-a732-4e6e-9e43-1b1f1f08ae40",
"47b6b1b4-ecfe-4008-b162-097aaa8eb759",  "c7f4aa96-1b2f-4ced-a265-cef17de64f8b",
"49e80721-0413-45e0-9a55-c2ee6093aaf4",  "cad86632-c0fe-4ff8-9d11-c17654e57b9f",
"4e46f879-ecd0-43de-88ee-a08e15c5d92c",  "cc12933c-a8d5-4fc4-8bef-56c214986d8a",
"4fe89313-8c7a-4c95-9b3b-155435d25c1a",  "d1b39917-03cd-4480-84fb-8a10de1d8f19",
"50ea2e67-dfe3-460a-b401-9d4d75d161e0",  "d257c9c6-aeb8-46a4-b722-62b20c9cf1b9",
"51639531-60ff-4905-8822-da241ac3e79b",  "db9606b2-abf6-4d4c-a0a6-7aa36b55a89f",
"52469c38-8ed4-4051-843b-6c265dba0623",  "df7cde7e-3b84-4bd9-bb2b-045afdef2b83",
"551291a3-63ff-4a02-bb1a-6fd797a072be",  "e28d8094-edc5-4390-a408-c5fad442b4f6",
"594ea824-e3c3-4fdd-9911-06c4164fabba",  "e542432f-6a2e-4b61-ab5a-de7c41dfdae5",
"5a022e5a-133a-4c29-bc0f-fa66ca5eae4d",  "e9e0e7d6-e07f-476f-a763-546d2830c026",
"5a1bb59f-efba-447f-80dd-5034b5771b22",  "e9f902c9-a331-4ec5-94bb-8f7147f5b509",
"5b76a848-eb5e-4974-8b6b-b372e0382f9c",  "ebd7af1a-a8ce-4589-bec4-6f8c3904d235",
"5cff8697-34ac-4bd2-b532-d7776da98dca",  "eca3ada9-4620-4fa6-97d3-7a8328d41c5f",
"5f81affe-0923-431f-a1f3-2598a6f4e1eb",  "ede168fa-9fea-432e-91dc-7de5c79c9fcb",
"6315b4e8-7874-43bf-b5d2-20ba56a35a47",  "f09905c6-161d-4ca1-9ef2-7af7441f9a1a",
"6c10fa29-6eef-402a-b864-501b2802a1c8",  "f1c47aa7-5b69-4467-897c-24151649bcf4",
"6c6afee9-0d13-423f-9bee-79e4cf4e3837",  "f683a560-fdee-4059-91de-6423da7a5300",
"6e72a55b-6b6a-4958-9128-a54f58df58eb",  "f7d25ca8-68d6-454e-9421-67ee5cc6f760",
"6ebb8870-c674-42eb-9d2f-b28993ec2d01","fb8dc6e6-56d0-4f95-849f-4c9007699ba8",
"6f6d3c16-87ba-4e62-b0b1-7722d9b98dc1", "fcba121d-352f-494b-86aa-a45ff1f283a3",
"6ff489c1-fa2b-44fc-99c5-fa28bf70f24d"]



@app.route('/wordcount/api/v1.0/get_wordcount', methods=['GET'])
def get_wordcount():
        res = [None]*(len(FILES))
        for i in range(len(FILES)):
            res_d = {}
            res[i] = count_file.delay(FILES[i],res_d,WORDS)
        while all(not result.ready() for result in res):
            pass
        for result in res:
            for word in result.get().keys():
                res_d[word] = res_d.get(word,0) + result.get()[word]
        return jsonify(res_d)


if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)
