var html='';
var data_response='';

$(function(){
	
	request( encodeURIComponent( location.search.replace('?','') ) );
	
	$(document).on('touchstart','.aside-btn',function(){
		zfx.showFullScreenMask();
		$('aside').addClass('show');
	});
	
	$(document).on('touchstart','aside>h3',function(){
		zfx.hideFullScreenMask();
		$('aside').removeClass('show');
	});
	
	$(document).on('touchstart','footer>.left',function(){
		zfx.showFullScreenMask();
		$('.cost').show();
	});
	
	$(document).on('touchstart','.cost>.close',function(){
		zfx.hideFullScreenMask();
		$('.cost').hide();
	});
	
	$(document).on('touchstart','.layer>.footer',function(){
		$('.layer').hide();
	});
	
	$(document).on('touchstart','nav>div',function(){
		var className=$(this).attr('class');
		$('.layer.'+className).show();
	});
	
	$(document).on('touchstart','footer>p.right',function(){
		zfx.showFullScreenMask();
		zfx.showLayer('link_us','参团咨询','微信公众号：baijiantravel<br/><br/>咨询热线：<a href="tel:17620322046">176 2032 2046</a>');
	});
	
	$(document).on('touchstart','#link_us>.close',function(){
		zfx.hideFullScreenMask();
		zfx.hideLayer('link_us');
	});
	
	$(document).on('touchstart','header>.share',function(){
		zfx.showFullScreenMask();
		zfx.showLayer('share_link','分享','请使用浏览器或微信自带的分享功能分享');
	});
	
	$(document).on('touchstart','#share_link>.close',function(){
		zfx.hideFullScreenMask();
		zfx.hideLayer('share_link');
	});
	
	$(document).on('touchstart',zfx.maskId,function(){
		zfx.hideFullScreenMask();
		$('aside').removeClass('show');
		$('.cost').hide();
		zfx.hideLayer('share_link');
		zfx.hideLayer('link_us');
	});
});

function request(request){
    $.ajax({
	    url:'http://m.beejeen.com/travel?key=' + request,
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
				add_event();
				weixin(data.weixin);
			}
	    },
	    error:function(xhr,textStatus){
	        console.log('错误')
	        console.log(xhr)
	        console.log(textStatus)
	    }
  	});
}

function add_event(){
	var script=document.createElement('script');
	script.src='../css/icon/iconfont.js';
	$('body').append(script); 
	
	$(document).on('click','aside>p',function(){
		console.log($(this).index()-1);
		zfx.hideFullScreenMask();
		$('aside').removeClass('show');
		var scrollTop=$('main>h2').eq($(this).index()-1).offset().top;
		$(document).scrollTop(scrollTop);
	});
	
}

function apppend_data(data,position){
	html=template('body_tpl', data);
	$(position).html(html);
}

function weixin(data){
	wx.config({
		debug: false, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
		appId: data.appId, // 必填，公众号的唯一标识
		timestamp: data.timestamp, // 必填，生成签名的时间戳
		nonceStr: data.nonceStr, // 必填，生成签名的随机串
		signature: data.signature,// 必填，签名，见附录1
		jsApiList: ['onMenuShareTimeline', 'onMenuShareAppMessage','onMenuShareQQ'] 
	});
	wx.ready(function(){
		var wx_share_imageurl=data_response.img,
			wx_share_url=data.url,
			wx_share_title='百见 ·'+data_response.name,
			wx_share_desc=data.intro;
		//分享到朋友圈
		wx.onMenuShareTimeline({
			title: wx_share_title,
    		link: wx_share_url,
    		imgUrl: wx_share_imageurl
		});
		
  		//分享给朋友
  		wx.onMenuShareAppMessage({
	  		title: wx_share_title,
	  		link: wx_share_url,
	  		desc: wx_share_desc,
	  		imgUrl: wx_share_imageurl
  		});
  		
  		//分享到QQ
		wx.onMenuShareQQ({
		  	title: wx_share_title,
		  	link: wx_share_url,
		  	desc: wx_share_desc,
		  	imgUrl: wx_share_imageurl
		});
	});
}


//蒙版模块
(function(){
	var zfx={
		//FullScreenMask
		hasFullScreenMask:false,
		maskId:'#full-screen-mask',
		
		showFullScreenMask:function(){
			var str='<div id="full-screen-mask" style="position:fixed;top:0;left:0;width: 100%;height: 100%;background: rgba(0,0,0,0.4);z-index: 998;cursor:pointer">'
			$('body').append(str);
			this.hasFullScreenMask=true;
		},
		
		hideFullScreenMask:function(){
			$('#full-screen-mask').remove();
			this.hasFullScreenMask=false;
		},
		
		toggleFullScreenMask:function(){
			this.hasFullScreenMask ? this.hideFullScreenMask() : this.showFullScreenMask();
			
		},
		//layer
		
		showLayer:function(id,title,content){
			var str='<section id="'+id+'" style="width: 5.2rem;height: 7.6rem;position: fixed;top: 50%;left: 50%;margin-top: -3.8rem;margin-left: -2.6rem;z-index: 999;background: #fff;">';
			str+='<div style="height: .68rem;line-height: .68rem;width: 100%;background: #f8f8f8;text-align: center;font-size: .3rem;box-shadow: 0 2px 2px rgba(0,0,0,.3);">'+title+'</div>';
			str+='<div class="close" style="width: .68rem;height: .68rem;line-height: .68rem;position: absolute;top: 0;right: 0;text-align: center;color: #fe413d;font-size: .34rem;cursor: pointer;">X</div>';
			str+='<p style="font-size: .24rem;padding: .3rem;">'+content+'</p>';
			str+='</section>';
			$('body').append(str);
		},
		
		hideLayer:function(id){
			$('#'+id).remove();
		},
		
		toggleLayer:function(id,title,content){
			$('#'+id).length>0?this.hideLayer(id):this.showLayer(id,title,content);
		},
	};
	
	//export api
	window.zfx=zfx;
})();
