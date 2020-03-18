 <h1>📱 Django_instagram 👩‍💻</h1>

-Django Instagram clone coding 진행

<b>계획</b>

~~1. photo 앱 만들기

~~2. 모델 설계하기 

3. views 설계하기
>> list페이지   
>> 상세페이지   
>> 삭제하기   
>> 수정하기   
>>  생성페이지   
 
4. url 연결   

5. template 만들기   
   * create/list/update/delete/detail      
   
6. 사진 업로드 기능    

7. success url을 get_absolute_url로 연동   

8. account 앱 생성 
   * 로그인/로그아웃 기능 구현하기   
   * 로그아웃 되었을 때는 create 및 sign out가 안 보이도록 구현(분기)      
 
9. 권한 문제 해결하기   
   * html 기준에서 해결하기   
   * 링크로 들어와도 안 되도록 해결       
       + view를 조정하기   
    
10. 댓글 기능 구현   
   * 댓글은 상세페이지에서 가능하게   
   * 소셜 댓글기능으로 구현      
 
11. 좋아요 버튼 만들기   
   * 스프라이트 이미지 기법 활용         
   * 클릭하면 색깔 바뀌도록 구현      
   * 로그인을 해야지 버튼 클릭이 되도록 하고 클릭을 하면 like count 올라가기   
   * like에 대한 정보를 저장하기   
   *  좋아요 counting 표시해주기   
   *  디테일 페이지에서 좋아요를 누르면 디테일 페이지에서 그대로 유지      
    >> view와 like에서의 분기   
    >> 레퍼러를 활용하여 해당 주소가 어디서부터 시작됬는지 확인      
    
12. 좋아요한 포스팅만 보기 기능 구현      

13. 포스팅 저장하기 기능 구현      

14. 저장한 포스팅 리스트 페이지 구현   

15. 좋아요한 포스팅 및 저장한 포스팅 리스트 보기는 로그인한 사람만 보여주기   
   *  view단에서 시행   
    > dispatch 활용   
    > LoginRequiredmixin   
   * html 활용   
 
16. my page에 내가 올린 사진들만 구현   

17. my page에 팔로우 기능 추가      
