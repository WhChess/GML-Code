x+= yatay_hiz;
y+= dikey_hiz;

if(!place_meeting(x, y+1, obj_duvar)){
	dikey_hiz += yercekimi
}

if(place_meeting(x+yatay_hiz, y, obj_duvar2)){
	while(!place_meeting(x+sign(yatay_hiz), y, obj_duvar2)){
		x += sign(yatay_hiz);
	}
	yatay_hiz = 0;
}
	
	
if(place_meeting(x, y+dikey_hiz, obj_duvar)){
	while(!place_meeting(x, y+sign(dikey_hiz), obj_duvar)){
		y += sign(dikey_hiz);
	}
	dikey_hiz = 0;
}