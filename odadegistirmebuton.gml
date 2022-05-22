// Step

if mouse_check_button_pressed(mb_left) {
    if collision_point(mouse_x, mouse_y, obj_buton, true, false) {
        room_goto(Room2);
    }
}
