var scrollTop=0;
var liNumber=0;
var liHeight=0;
var html='';
var data_response='';

$(function(){
	
	request( encodeURIComponent( location.search.replace('?','') ) );
	
	$(document).on('click','nav li',function(){
		$('nav li').removeClass('current');
		$(this).addClass('current');
		$('main>div').hide().removeClass('current')
		.eq( $(this).index() ).show().addClass('current')
		.find('.left>p').removeClass('current')
		.eq(0).show().addClass('current')
		.end()
		.end()
		.find('.right>div').hide().eq(0).show();
	});
	
	$(document).on('click','nav .up',function(){
		liNumber=$('nav>section>ul>li').length;
		liHeight=$('nav>section>ul>li').height()+1;
		if( scrollTop == 0 ){
			scrollTop=liHeight*( liNumber -4 );
		}else if( (scrollTop-=$('nav>section>ul').height()) < 0  ){
			scrollTop=0;
		}
		$('nav>section>ul').scrollTop( scrollTop );
	});
	
	$(document).on('click','nav .down',function(){
		liNumber=$('nav>section>ul>li').length+1;
		liHeight=$('nav>section>ul>li').height();
		scrollTop+=$('nav>section>ul').height();
		console.log("scrollTop:"+scrollTop);
		if( scrollTop>liHeight*( liNumber -1 ) ){
			scrollTop=0;
		}
		$('nav>section>ul').scrollTop( scrollTop );
		
	});
	
	$(document).on('click','main .left>p',function(){
		$('main>div>.left>p').removeClass('current');
		$(this).addClass('current');
		var n= ( $(this).index()-1 )/2; 
		console.log(n);
		$('main>div.current>.right>div').hide().eq( n ).show();
	});
	
});

function request(request){
    $.ajax({
	    url:'http://www.beejeen.com/travel?key=' + request,
	    type:'get',
	    async:true,
	    timeout:5000,
	    dataType:'json',
	    success:function(data,textStatus,jqXHR){
	        console.log('成功')
	        console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
	        data_response=data;
			if(!!data.link){
				location.href=data.link;
			}else{
			 	apppend_data(data,'body');
			 	var script=document.createElement('script');
				script.src='../css/icon/iconfont.js';
				$('body').append(script); 
			}
	    },
	    error:function(xhr,textStatus){
	        console.log('错误')
	        console.log(xhr)
	        console.log(textStatus)
	    }
  	});
}

function apppend_data(data,position){
	html=template('body_tpl', data);
	$(position).html(html);
}