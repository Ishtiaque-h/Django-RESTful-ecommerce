$(document).ready(function(){											
				var menuHovered = false;
				var newHover = true;
				var submenuHovered = false;					
				var lastIndex = 0;
				$("a.dropdown-toggle").mouseover(function(){
						if(lastIndex!=$(this).index("a.dropdown-toggle")){
							$(".dropdown-menu").slideUp(300);
						}
						lastIndex = $(this).index("a.dropdown-toggle");
						$(".dropdown-menu:eq("+lastIndex+")").slideDown(300);
						$(this).attr("aria-expanded","true");
						$(this).parent("li.dropdown").addClass("show");
						menuHovered = true;
						newHover = true;
				}).mouseleave(function(){					
						menuHovered = false;	
						setTimeout(function(){
								if(!submenuHovered && !newHover){
									$(".dropdown-menu:eq("+lastIndex+")").slideUp(300);
									$(this).attr("aria-expanded","false");
									$(this).parent("li.dropdown").removeClass("show");
									newHover = false;						
								}								
						},800);							
				});				
				
				$(".dropdown-menu").mouseover(function(){
					submenuHovered = true;
				}).mouseleave(function(){
					submenuHovered = false;	
					if(!menuHovered){
						$(this).slideUp(300);
						$(this).prev("a.dropdown-toggle").attr("aria-expanded","false");
						$(this).prev("a.dropdown-toggle").parent("li.dropdown").removeClass("show");
					}
				});
				
				$(".not-dropdown").mouseover(function(){
					$(".dropdown-menu:eq("+lastIndex+")").slideUp(300);
					$("a.dropdown-toggle:eq("+lastIndex+")").attr("aria-expanded","false");
					$("a.dropdown-toggle:eq("+lastIndex+")").parent("li.dropdown").removeClass("show");
				});
								
				$("div, li, a").on("mouseover",function(){
					var className = $(this)[0].classList[0];
					if(className!="dropdown-toggle" && className!= "dropdown" && className!= "navbar-collapse" 
					&& className!= "dropdown-menu" && className!= "nav-link" && className!= "nav-item" 
					&& className!="dropdown" && className != "dropdown-item" && className != "collapse"
					&& className != "myMenuWrapper" && className!="topMenu" && className!="crewMain"){
						//$(".dropdown-menu:eq("+lastIndex+")").slideUp(300);
						$("a.dropdown-toggle:eq("+lastIndex+")").attr("aria-expanded","false");
						$("a.dropdown-toggle:eq("+lastIndex+")").parent("li.dropdown").removeClass("show");
					}	
		});	
});