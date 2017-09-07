var display_append='';
var json=null;
var str='';
var data_city='';
var data_response='';

$(function(){
	
	request( encodeURIComponent( location.search.replace('?','') ) );
	
	$('#input-search').click(function(){
		search( encodeURIComponent( $('#input-text').val() ) );
	});
	
	$('#input-text').on('keypress',function(e){ 
        if(e.keyCode == 13){  
			search( encodeURIComponent( $('#input-text').val() ) );
        }
     });
	
	$('#language').click(function(){
    	localStorage.setItem('beejeen-language','cn');
    	location.href=location.href.replace('city-en.html','city-cn.html');
    });
	
	$('.main>.tab-nav').on('mouseenter','li',function(){
		$(this).addClass('current').siblings('li').removeClass('current');
		$('#display_append>div').hide();
		$('#'+$(this).attr('data-type')).show(0);
	});
});


//请求函数
function request(request){
    $.ajax({
	    url:'http://www.beejeen.com/city?key=' + request,
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
				location.href=data.link.replace('.html','-en.html');
			}else{
				analysis_data(data);
				add_event();
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


//解析数据
function analysis_data(data){
	data_city=data.city;
	$('#open-iframe').attr('href','tour.html?'+data_city.iframe_type+'&key='+data_city.href_name);
	$('#display-title').text(data_city.name );
	document.title = data_city.name ;
	$('#city-description span').html( data_city.text );
	$('body').append( template('nav_tpl', data) );
	changeMain(data,'display_append','en');
}

//向页面填充数据
function apppend_data(obj,position,language){
	str='';
	for(var i=0 ; i<obj.length;i++){
		json=obj[i];
		str+='<a href="tour.html?'+json['table']+'&key='+json.href_name+'" target="_blank" >'+
				'<div class="col-xs-12 col-sm-6 col-md-4 col-lg-3">'+
					'<div class="main-cell">'+
						'<div class="main-cell-imgBox">'+
							'<img class="main-cell-img" src="'+json.img+'" />'+
						'</div>'+
						'<div class="main-cell-textBox">'+
							'<div class="main-cell-iconBox">'+
								'<div class="icon-views"></div>'+
								'<span class="main-views-num">'+json.view+'</span>'+
								'<div class="icon-likes"></div>'+
								'<span class="main-likes-num">'+json.like+'</span>'+
							'</div>'+
							'<p class="main-cell-name">'+json.name+'</p>'+
							'<div class="person-head-icon"></div>'+
						'</div>'+
					'</div>'+
				'</div>'+
			'</a>';
	}
								
	$('#'+position).append('<div id="'+json['type']+'" style="display:none;">'+str+'</div>');

}

function changeMain(data,position,language){
	$('#'+position).html('');
	apppend_data(data.hot,position,language);
	$('#hot').show();
	apppend_data(data.sight,position,language);
	apppend_data(data.hotel,position,language);
	apppend_data(data.activity,position,language);
	apppend_data(data.restaurant,position,language);
}


function add_event(){
	
	$('.destination').on('click',function(){
    	$('#navigation').show();
    	zfx.showFullScreenMask();
//  	$('html').addClass('fixed');
    	$('#navigation>ul.nav-item>li').eq(0).addClass('current').siblings().removeClass('current');
    	$('#navigation>ul.nav-bar>li').eq(0).addClass('current').siblings().removeClass('current');
    });
    
    $('#navigation>ul.nav-bar>li').on('click',function(){
    	$(this).addClass('current').siblings().removeClass('current');
    	$('#navigation>ul.nav-item>li').eq( $(this).index() ).addClass('current')
    	.siblings().removeClass('current');
    });
    
    $('.nav-close').on('click',function(){
    	$('#navigation').hide();
    	zfx.hideFullScreenMask();
//  	$('html').removeClass('fixed');
    });
    
    $('#navigation span').on('click',function(){
    	search( encodeURIComponent( $(this).text() ) );
    });
    
    $('#navigation>input').on('click',function(){
    	search( encodeURIComponent( $(this).val() ) );
    });
    
    $('#navigation>input').on('keypress',function(e){
        if(e.keyCode == 13){  
			search( encodeURIComponent( $(this).val() ) );
        }
     });
    
}


//全屏、蒙版 封装模块
(function(){
	var zfx={

		//FullScreenMask
		hasFullScreenMask:false,
		maskId:'#full-screen-mask',
		
		showFullScreenMask:function(){
			var str='<div id="full-screen-mask" style="position:fixed;top:0;left:0;width: 100%;height: 100%;background: rgba(0,0,0,0.4);z-index: 1000;"></div>'
			$('body').append(str);
			this.hasFullScreenMask=true;
		},
		
		hideFullScreenMask:function(){
			$('#full-screen-mask').remove();
			this.hasFullScreenMask=false;
		},
		
		toggleFullScreenMask:function(){
			this.hasFullScreenMask ? this.hideFullScreenMask() : this.showFullScreenMask();
			
		}
	};
	
	//export api
	window.zfx=zfx;
})();
