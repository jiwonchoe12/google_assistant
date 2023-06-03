function getPerplexity(url){ // 서버에 요청을 보내는 함수
  const response = fetch(url); // fetch를 통해서 요청을 보냄 | fetch는 비동기함수
  return response.then(res => res.json()); // 요청에 대한 답변을 리턴함. (json 형식으로)
}

function getKoGPT(title){
    const response = fetch(title); // fetch를 통해서 요청을 보냄 | fetch는 비동기함수
    return response.then(res => res.json()); 
  }

async function exec(){ //동기함수이다.
    var title = document.getElementById("APjFqb").value;
    var title_link = "http://127.0.0.1:5000/title/" + title;
    try {
      gpt_answer = await getKoGPT(title_link);
      console.log(gpt_answer);
      document.getElementsByClassName("NhRr3b aBOYt")[0].innerHTML = document.getElementsByClassName("NhRr3b aBOYt")[0].innerHTML + '<div style=\"display:block\">' + gpt_answer + '</div>';
      }
    catch(error){
      console.log(error);
    }

    var elements = document.getElementsByTagName("h3"); //각각의 링크를 찾기 위한 첫번째 단계, 각각의 링크의 제목을 추출한다
    for (i = 0; i < elements.length; i++) {
        var element = elements[i];
        if(typeof element.parentElement.href == "undefined" || element.parentElement.href == null || element.parentElement.href == "") //링크가 없는 것에 대한 예외처리
            continue;
        var link = element.parentElement.href; // 링크 저장
        link = link.replaceAll('https://', ''); // 링크를 변환
        link = link.replaceAll('http://', '');
        link = link.replaceAll('/', '~');
        var apiLink = "http://127.0.0.1:5000/api/" + link; //서버에 대한 주소에다가 요청 주소를 저장한다.
        console.log(apiLink);
        try {
            data = await getPerplexity(apiLink); // 실제로 서버에 요청을 보내는 부분 | Await는 동기 처리를 위해 사용함.
            console.log(data);
            elements[i].innerHTML = elements[i].innerHTML + '<font color=\"red\">' + data + '</font>';
          }
          catch(error){
            console.log(error);
          }
      }
  }
exec();