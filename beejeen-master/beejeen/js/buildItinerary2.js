var html='';
var data_response='';

$(function(){
	
	$(document).on('click','nav>ul>li',function(){
		$(this).addClass('current')
		.siblings().removeClass('current');
	});
	
	$(document).on('click','#country_list>li',function(){
		$(this).addClass('now')
		.parent('#country_list').hide();
		$( '#'+ $(this).attr('data-id') ).show().addClass('show');
	});
	
	$(document).on('click','.dayEdit>.city-list>li>i',function(){
		var text=$(this).siblings('span').html().split('&nbsp;')[0];
		var append = $('nav>ul>li.current>p>span');
		if( append.text() == '暂未添加' ){
			append.text(text);
		}else{
			append.append('-'+text);
		}
		$(this).removeClass('icon-right').addClass('icon-true')
		.parent('li').addClass('selected').removeClass('current');
		$('#country_list>li.now').addClass('selected').removeClass('current')
		.children('i').removeClass('icon-right').addClass('icon-true');
	});
	
	$(document).on('click','.dayEdit>p',function(){
		$(this).siblings('.show').hide().removeClass('show')
			.siblings('#country_list').show();
		$('#country_list>li.now').removeClass('now');
	});
	
	$('.city-list>li').on('mouseenter',function(){
		if( $(this).hasClass('selected') ){
			$(this).children('i').removeClass('icon-true').addClass('icon-plus');
		}
	});
	
	$('.city-list>li').on('mouseleave',function(){
		if( $(this).hasClass('selected') ){
			$(this).children('i').removeClass('icon-plus').addClass('icon-true');
		}
	});
});
