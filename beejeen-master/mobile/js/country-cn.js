﻿var html='';
var data_response='';
	
$(function(){

	request( encodeURIComponent( location.search.replace('?','') ) );
	
});

function request(request){
    $.ajax({
	    url:'http://m.beejeen.com/country?key=' + request,
	    type:'get',
	    async:true,
	    timeout:5000,
	    dataType:'json',
	    beforeSend:function(xhr){
	        console.log(xhr)
	        console.log('发送前')
	    },
	    success:function(data,textStatus,jqXHR){
	        console.log('成功')
	        console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
	        data_response=data;
			if(!!data.link){
				location.href=data.link.replace('.html','-cn.html');
			}else{
				document.title = data.country.name ;
			 	apppend_data(data,'body');
			 	addEvent();
			}
	    },
	    error:function(xhr,textStatus){
	        console.log('错误')
	        console.log(xhr)
	        console.log(textStatus)
	    },
	    complete:function(){
	        console.log('结束')
	    }
  	});
}

function apppend_data(data,position){
	html=template('body_tpl', data);
	$(position).html(html);
}

function addEvent(){
	
	$('#input-text').on('search',function(e){
		search( encodeURIComponent( $('#input-text').val() ) );
     });
     
    $('header>.language').on('click',function(){
    	localStorage.setItem('beejeen-language','en');
    	location.href=location.href.replace('country-cn.html','country-en.html');
    });
}
