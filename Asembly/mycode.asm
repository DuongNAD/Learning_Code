.model small
.stack 100h
.data
board db 20 dup (10 dup (0))
cur_x db 4
cur_y db 0
cur_shape db 0
cur_rot db 0
timer_flag db 0
tick_count db 0
score dw 0
game_over db 0
shapes label byte
 db 0,0, 1,0, 2,0, 3,0    ; I hor
 db 0,0, 0,1, 0,2, 0,3    ; I ver
 db 0,0, 1,0, 2,0, 3,0    ; I hor
 db 0,0, 0,1, 0,2, 0,3    ; I ver
 db 0,0, 1,0, 0,1, 1,1    ; O
 db 0,0, 1,0, 0,1, 1,1    ; O
 db 0,0, 1,0, 0,1, 1,1    ; O
 db 0,0, 1,0, 0,1, 1,1    ; O
 db 0,0, 1,0, 2,0, 0,1    ; L rot0
 db 0,0, 0,1, 0,2, 1,2    ; L rot1
 db 2,0, 0,1, 1,1, 2,1    ; L rot2
 db 0,0, 1,0, 1,1, 1,2    ; L rot3
 db 0,0, 1,0, 2,0, 1,1    ; T rot0
 db 0,0, 0,1, 1,1, 0,2    ; T rot1
 db 0,1, 1,1, 2,1, 1,0    ; T rot2
 db 1,0, 0,1, 1,1, 1,2    ; T rot3
 db 0,0, 1,0, 1,1, 2,1    ; Z rot0
 db 1,0, 0,1, 1,1, 0,2    ; Z rot1
 db 0,0, 1,0, 1,1, 2,1    ; Z rot2
 db 1,0, 0,1, 1,1, 0,2    ; Z rot3
menu_msg db '1. Bat dau tro choi',13,10,'2. Huong dan',13,10,'3. Thoat',13,10,'$'
inst_msg db 'Phim A: Trai, D: Phai, S: Xuong, W: Xoay, P: Tam dung, Q: Thoat',13,10,'Moi hang xoa +10 diem',13,10,'$'
game_over_msg db 'Game Over! Diem: $'
restart_msg db 'Nhan R de restart, Q de quay menu',13,10,'$'
score_msg db 'Diem: $'
old_timer dd ?
.code
main proc
    mov ax,@data
    mov ds,ax
    ; Hook int 1Ch
    mov ah,35h
    mov al,1ch
    int 21h
    mov word ptr old_timer,bx
    mov word ptr old_timer+2,es
    mov ah,25h
    mov al,1ch
    push ds
    mov dx,cs
    mov ds,dx
    mov dx,offset timer
    int 21h
    pop ds
    call clrscr
    call show_menu
game_loop:
    ; KHONG clear_board o day nua!
    call generate_piece
    call draw_piece
    call game_main_loop
    cmp game_over,1
    je end_game
    jmp game_loop
end_game:
    call show_game_over
    mov ah,0
    int 16h
    cmp al,'r'
    je restart
    cmp al,'q'
    je menu_return
    jmp end_game
restart:
    mov game_over,0
    mov score,0
    call clear_board  ; Them day de xoa board cu
    call clrscr
    call draw_boundry
    call show_score
    jmp game_loop
menu_return:
    call clrscr
    call show_menu
exit:
    ; Restore int 1Ch
    mov ah,25h
    mov al,1ch
    push ds
    lds dx,dword ptr old_timer
    int 21h
    pop ds
    mov ax,4c00h
    int 21h
main endp
; ... (cac proc khac giu nguyen, chi sua check_collision, place_piece, draw_piece, draw_board, land_piece)
timer proc
    push ax
    inc tick_count
    cmp tick_count,9
    jb no_drop
    mov timer_flag,1
    mov tick_count,0
no_drop:
    pop ax
    pushf
    call dword ptr old_timer
    iret
timer endp
; Cac proc khac nhu clrscr, show_menu, draw_boundry, generate_piece, game_main_loop, kb_input giu nguyen hoan toan
; SUY DUNG CHINH:
check_collision proc
    mov al,1
    push si
    mov si,offset shapes
    xor ax,ax
    mov al,cur_shape
    mov bl,32
    mul bl
    add si,ax
    xor ax,ax
    mov al,cur_rot
    mov bl,8
    mul bl
    add si,ax
    mov cx,4
loop_check:
    mov ah,[si]      ; rel x
    mov al,[si+1]    ; rel y
    add ah,cur_x     ; abs x
    add al,cur_y     ; abs y
    cmp ah,0
    jl collision
    cmp ah,9
    jg collision
    cmp al,0
    jl collision
    cmp al,19
    jg collision
    ; Tinh index = y*10 + x MA KHONG PHA AH (x)
    mov cl,al        ; cl = y
    xor al,al
    mov al,10
    mul cl           ; ax = 10*y
    add al,ah        ; + x (low)
    adc ah,0
    mov bx,ax
    cmp board[bx],1
    je collision
    add si,2
    loop loop_check
    mov al,0
collision:
    pop si
    ret
check_collision endp
place_piece proc
    push si
    mov si,offset shapes
    xor ax,ax
    mov al,cur_shape
    mov bl,32
    mul bl
    add si,ax
    xor ax,ax
    mov al,cur_rot
    mov bl,8
    mul bl
    add si,ax
    mov cx,4
loop_place:
    mov ah,[si]      ; rel x
    mov al,[si+1]    ; rel y
    add ah,cur_x     ; abs x
    add al,cur_y     ; abs y
    ; Tinh index nhu tren
    mov cl,al        ; cl = y
    xor al,al
    mov al,10
    mul cl           ; ax = 10*y
    add al,ah        ; + x
    adc ah,0
    mov bx,ax
    mov board[bx],1
    add si,2
    loop loop_place
    pop si
    ret
place_piece endp
draw_piece proc
    push si
    mov si,offset shapes
    xor ax,ax
    mov al,cur_shape
    mov bl,32
    mul bl
    add si,ax
    xor ax,ax
    mov al,cur_rot
    mov bl,8
    mul bl
    add si,ax
    mov cx,4
loop_draw:
    mov ah,[si]
    mov al,[si+1]
    add ah,cur_x
    add al,cur_y
    mov dh,al
    add dh,2
    mov dl,ah
    add dl,30
    mov ah,2
    mov bh,0
    int 10h
    mov ah,9
    mov al,0DBh      ; Full block ¦ thay #
    mov bh,0
    mov bl,0Eh       ; Mau vang
    mov cx,1
    int 10h
    add si,2
    loop loop_draw
    pop si
    ret
draw_piece endp
; Xoa draw_piece o day trong land_piece (game_main_loop)
; Trong game_main_loop land_piece:
; dec cur_y
; call place_piece
; REM call draw_piece  <- XOA
; call clear_lines
; call draw_board
draw_board proc
    mov bx,0
loop_rows_draw:
    mov cl,0
loop_cols_draw:
    mov ax,bx
    mov ah,0
    mov dl,10
    mul dl
    add al,cl
    adc ah,0
    mov si,ax
    mov dh,bl
    add dh,2
    mov dl,cl
    add dl,30
    mov ah,2
    mov bh,0
    int 10h
    mov ah,9
    cmp board[si],1
    je draw_block
    mov al,' '
    jmp draw_it
draw_block:
    mov al,0DBh      ; Full block
draw_it:
    mov bh,0
    mov bl,0Eh
    mov cx,1
    int 10h
    inc cl
    cmp cl,10
    jl loop_cols_draw
    inc bx
    cmp bx,20
    jl loop_rows_draw
    ret
draw_board endp
; Cac proc con lai (clear_piece, clear_lines, etc.) giu nguyen
clear_piece proc
    push si
    mov si,offset