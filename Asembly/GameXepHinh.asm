.Model Small

;;;;;;;;;;;; macros ;;;;;;;;;;

draw_row Macro x,y,z,color  ;x - row, y - begining column, z - ending column
    Local L1
    ; draws a line in row x from col y to col z
    MOV AH, 0CH
    MOV AL, color
    MOV CX, y
    MOV DX, x
L1: INT 10h
    INC CX
    CMP CX, z
    JL L1
    EndM

    draw_column Macro x,y,z,color ;x - column, y - begining row, z - ending row
    Local L2
    ; draws a line col y from row y to row z
    MOV AH, 0CH
    MOV AL, color
    MOV CX, x
    MOV DX, y
L2: INT 10h
    INC DX
    CMP DX, z
    JL L2
    EndM

    display_string Macro x,row,column,length,color

    push ax
    push bx

    ; *** SUA LOI: Khong khoi tao AX, ES o day ***
    ; MOV AX, @DATA
    ; MOV ES, AX  
    
    MOV AH, 13H ; WRITE THE STRING
    MOV AL, 0H; ATTRIBUTE IN BL, MOVE CURSOR TO THAT POSITION
    XOR BH,BH ; VIDEO PAGE = 0
    mov bl,color
    
    MOV BP, OFFSET x ; ES: BP POINTS TO THE TEXT
    MOV CX, length ; LENGTH OF THE STRING
    MOV DH, row ;ROW TO PLACE STRING
    MOV DL, column ; COLUMN TO PLACE STRING
    INT 10H
    
    pop bx
    pop ax
    
    EndM  
    
    
draw_block Macro start_row, end_row, start_column, end_column, color_block
    Local along_row, row_loop ; Can them 1 nhan (label) noi bo
    
    PUSH AX  ; Bao toan cac thanh ghi se su dung
    PUSH CX
    PUSH DX
    
    MOV DX, start_row   ; DX giu gia tri HANG (row) hien tai
  
along_row: ; Lap qua cac hang (tu tren xuong duoi)
    
    ; --- Day la logic cua 'draw_row' duoc chep vao ---
    MOV AH, 0CH
    MOV AL, color_block  ; Dung truc tiep tham so 'color_block'
    MOV CX, start_column ; Dung truc tiep tham so 'start_column'
    ; DX da chua dung gia tri hang (row)
    
row_loop: ; Lap qua cac cot (tu trai sang phai)
    INT 10h
    INC CX
    CMP CX, end_column   ; Dung truc tiep tham so 'end_column'
    JL row_loop
    ; --- Ket thuc logic 'draw_row' ---
    
    INC DX  ; Di chuyen xuong hang tiep theo
    CMP DX, end_row
    JLE along_row ; Lap lai neu chua ve xong
    
    POP DX  ; Khoi phuc cac thanh ghi
    POP CX
    POP AX
        
EndM

;write a draw piece macro - task for tomorrow (angela) 
  
draw_full_block Macro pattern_name, color, compare
    Local draw
    
    PUSH SI ; *** SUA: Dung SI lam con tro ***
    PUSH AX ; Can AX de tinh dia chi ket thuc
    
    LEA SI, pattern_name ; SI la con tro co so
    LEA AX, pattern_name 
    ADD AX, compare      ; AX la dia chi offset ket thuc (vi du: offset(pattern_name) + 24)
    
    draw:
        ; *** SUA: Truy cap bo nho truc tiep qua con tro SI ***
        ; Macro 'draw_block' se nhan [SI], [SI+2],...
        ; va se mo rong thanh 'MOV DX, [SI]', 'MOV DX, [SI+2]'...
        ; Day la cu phap Assembly hoan toan hop le.
        draw_block [SI], [SI+2], [SI+4], [SI+6], color
        
        ADD SI, 8            ; Tang con tro len 8 byte (4 words)
        CMP SI, AX           ; So sanh con tro hien tai voi dia chi ket thuc
        JLE draw
        
    POP AX
    POP SI ; *** SUA: Khoi phuc SI ***
    
EndM
        

 
update_block Macro pattern_name, blockToBeUpdated
    local while
    
    push ax
    push bx
    push cx
    mov cx,16
    mov bx,0
    
    while:
        mov ax,pattern_name[bx]
        mov blockToBeUpdated[bx],ax
        add bx,2
        ; cmp bx,24
        loop while
          
    pop cx
    pop bx
    pop ax
    EndM
    
    

    
;pull row downwards
modify_row_elements Macro pattern_name, delta, number_of_blocks ; delta = dhakkar amount :3
    local ghuro,exit
    
    push ax
    push bx
    PUSH CX
    PUSH DX
    
    
    ;modify row elements
    
    mov cx,number_of_blocks
    mov bx,0
    
    ghuro:
        
        xor ax,ax
        xor dx,dx
        
        MOV ax,pattern_name[bx]
        add ax,delta
        MOV pattern_name[bx],ax
        
        add bx,2
        
        MOV dx,pattern_name[bx]
        add dx,delta
        MOV pattern_name[bx],dx
        
        add bx,6
        
        loop ghuro
  
    
    exit:
        pop dx
        pop cx
        pop bx
        pop ax

    EndM  
    
;;;;;;;;;;;;;; ;daine bame dhakka dibo B| ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    
modify_column_elementsD Macro pattern_name, delta, compare ; delta = dhakkar amount :3
    local byebye,shorao
    
    
   push ax
   push bx
   PUSH CX
   PUSH DX
    
    ;modify column elements
    
    mov bx,4
    
    shorao: 
        
    
    ; cmp pattern_name[30],345
    ;    jg byebye
   koop:     
        MOV cx,pattern_name[bx]
        add cx,delta
        cmp cx,190 ; *** SUA: 380 -> 190 ***
        jge byebye
        MOV pattern_name[bx],cx
        
        add bx,2
        MOV dx,pattern_name[bx]
        
        add dx,delta
        MOV pattern_name[bx],dx
        
        add bx,6
        xor cx,cx
        xor dx,dx
        
        cmp bx,compare
        jle shorao
        
        
  
    byebye:

        
        pop dx
        pop cx
        pop bx
        pop ax
        
    EndM    
    
    
modify_column_elementsA Macro pattern_name, delta, compare
    local byebye,shorao
    
        push ax
        push bx
        PUSH CX
        PUSH DX
    
    ;modify column elements
    
    mov bx,4
    
    shorao:
        
        
        MOV cx,pattern_name[bx]
        sub cx,delta
        cmp cx,114 ; *** SUA: 228 -> 114 (hoac 110 tuy y) ***
        jle byebye
        MOV pattern_name[bx],cx
        
        add bx,2
        MOV dx,pattern_name[bx]
        sub dx,delta
        MOV pattern_name[bx],dx
        
        
        add bx,6
        xor cx,cx
        xor dx,dx
        
        cmp bx,compare
        jle shorao
        

    byebye:
        
        ;sub cx,2             ; offset move
        ;MOV pattern_name[bx],cx
        
            pop dx
            pop cx
            pop bx
            pop ax
        

    EndM  
   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;dhakkadhakki sesh B| 
    

 
time_delay Macro pattern_name
    Local tt, sesh ; *** SUA: Chi can 2 label la du ***
  ;  push ax
    push bx
    push cx
    push dx
    
tt:
    ; --- SUA: Xoa bo 10 vong lap cho thua ---
    CMP timer_flag, 1   ; Cho 1 nhip dong ho
    JNE tt
    MOV timer_flag, 0
    
    CALL move_block     ; Goi ham xu ly (bao gom ca trong luc)
    
    mov bx, pattern_name[16]
    cmp bX, 158 ; Kiem tra xem khoi cham day chua
    jg sesh     ; Neu cham day -> thoat macro
    
    JMP tt      ; Neu chua cham -> Lap lai, cho nhip tiep theo
        
    ; --- XOA CAC DONG tt2 den tt11 ---

sesh:
    
    ;  mov [block_boshche],1 
    
    pop dx
    pop cx
    pop bx
EndM  
    
  

.Stack 100h


.Data
new_timer_vec   dw  ?,?
old_timer_vec   dw  ?,?
a1              dw ?
a2              dw ?
b1              dw ?
b2              dw ?
score           dw ?
flagg           db 0
color           db 4
seshs           db 0
next_color      db 9
line            dw 0
timer_flag      db  0
vel_x           dw  1
vel_y           dw  1
boxer_a         dw  ?    ; these two vars deal with current upper and lower row bounds
boxer_b         dw  ?    ; of the single blocks

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                       strings that will be displayed                   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

msg_next        db "Next$",0
msg_left        db "A - Left$"
msg_right       db "D - Right$"
msg_rotate      db "S - Jump Fast$"
msg_quit        db "Q - Quit$"
msg_lines       db "Lines$"
msg_score       db "Score$"
msg_game_over   db "Game Over!$"
msg_tetris      db "TETRIS$"
game_score      db "0000$"



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

screen_width        dw 320
column_limit        dw 0
row_limit           dw 0
block_width         dw 10
block_height        dw 5
block_boundary      dw 153
block_boshche       dw 0
box_medium          dw 100
current_row         dw 0
current_block       dw 0
next_block          dw 0


;;;;;;;; time ;;;;;;;;

;;;;;;;;;;;;; blocks ;;;;;;;;;;;;;;;;;;;;;;
; *** SUA: Tat ca cac toa do X (cot) da duoc chia 2 ***

horizontal          dw 51,56,145,150  ; (290,300)
                    dw 51,56,150,155  ; (300,310)
                    dw 51,56,155,160  ; (310,320)
                    dw 0,0,0,0
                    

next_horizontal     dw 71,76,215,220  ; (430,440)
                    dw 71,76,220,225  ; (440,450)
                    dw 71,76,225,230  ; (450,460)
                    dw 0,0,0,0
                    
                    
          
vertical            dw 51,56,142,147  ; (285,295)
                    dw 56,61,142,147  ; (285,295) 
                    dw 61,66,142,147  ; (285,295)
                    
                    
                    
                    
T_shape             dw 51,56,145,150  ; (290,300)
                    dw 51,56,150,155  ; (300,310)
                    dw 51,56,155,160  ; (310,320)
                    dw 56,62,155,160  ; (310,320)
                    
      
L_shape             dw 51,56,145,150  ; (290,300)
                    dw 51,56,150,155  ; (300,310)
                    dw 51,56,155,160  ; (310,320)
                    dw 45,50,145,150  ; (290,300)
                    
                    
next_L_shape        dw 71,76,215,220  ; (430,440)
                    dw 71,76,220,225  ; (440,450)
                    dw 71,76,225,230  ; (450,460)
                    dw 65,70,215,220  ; (430,440)


                    
Ulta_L              dw 51,56,145,150  ; (290,300)
                    dw 51,56,150,155  ; (300,310)
                    dw 51,56,155,160  ; (310,320)
                    dw 57,64,155,160  ; (310,320)
                    

Ulta_T              dw 51,56,145,150  ; (290,300)
                    dw 51,56,150,155  ; (300,310)
                    dw 51,56,155,160  ; (310,320)
                    dw 45,50,155,160  ; (310,320)
                    
                    
right_L             dw 51,56,145,150  ; (290,300)
                    dw 51,56,150,155  ; (300,310)
                    dw 51,56,155,160  ; (310,320)
                    dw 45,50,155,160  ; (310,320) 
                    
                    
next_right_L        dw 71,76,215,220  ; (430,440)
                    dw 71,76,220,225  ; (440,450)
                    dw 71,76,225,230  ; (450,460)
                    dw 65,70,225,230  ; (450,460)
                    
                      
currentBlock        dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0

next_piece          dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    
offsetArray         dw 20,20,140,140
                    dw 20,20,140,140
                    dw 20,20,140,140 
                    dw 20,20,140,140 
                    
temp_nxt_piece      dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    
                  
choose_random_piece   dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    
                    
zero_matrix         dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                    dw 0,0,0,0
                      
                    

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

.CODE

MAIN PROC 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                       Initialization                                  ;


    MOV AX,@DATA
    MOV DS,AX ;DATA INITIALIZATION HOYE GESE
    MOV ES,AX ; *** THEM DONG NAY DE KHOI TAO ES ***

; set CGA 640x200 high res mode
    mov AH,0
    MOV AL,13h ; *** SUA LOI: Chuyen tu 0Eh sang 13h (320x200) ***
    int 10h
    
; set keyboard parameters to be most responsive
    ;mov ax,0305h
    ; xor bx,bx
    ; int 16h
    
   ;set bgd color 
    ; *** SUA LOI: Vô hi?u hóa ng?t không du?c h? tr? ***
    ; mov ah,0bh
    ; mov bh,0
    ; mov bl,15
    ; int 10h
    
;generate initial piece
    
    ;call proc....

;display screen stuffs    
  
    call procedure_draw_screen
    
    ; *** SUA: Toa do X (cot) chia 2 ***
    draw_block 158,164,118,180,0fh ; (236,360) -> (118,180)
    
    
    ;draw a block at roof middle position
    
    ;MOV BL,13
    ;draw_block 51,71,300,310,04h
    ;draw_block 51,71,320,330,08h
    ;draw_block 51,71,330,340,09h
    ;draw_block 160,170,300,310,09h
      
;;;;;;;;;;;;;;;; gravity niye khela hobe -_- ;;;;;;;;;;;;;;

    ; set up timer interrupt vector
    MOV new_timer_vec, offset timer_tick
    MOV new_timer_vec+2, CS
    MOV AL, 1CH; interrupt type
    LEA DI, old_timer_vec
    LEA SI, new_timer_vec
    CALL setup_int
  
    
    ;PUSH CX
    ;PUSH DX
    ;mov cx,horizontal[4] ;starting point,not yet done for each block,have to fix this one
    ;mov dx,horizontal[6]
    ;
    ;MOV boxer_a,cx
    ;MOV boxer_b,dx
    ;
    ;pop dx
    ;pop cx
    
;   draw_block boxer_a,boxer_b,320,330,15
;   CALL move_block
;   MOV AH,01h
;   INT 16H

    ;copy horizontal array to currentBlock
    ;draw_block 158,163,235,360,08h
    mov score,0
    ;update_block L_shape, currentBlock
    
    ;draw_block 158,163,235,360,08h
    
    ;show_next_piece T_shape,24                                  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; modify this
    
    ;draw_block 158,163,235,360,08h
    
    ;for horizontal one 
    ;time_delay currentBlock
    
    ; time_delay vertical
    ; time_delay L_shape
    
    ;;;infinite loop e fele diyechi dada;;; :p
    ;draw_block 158,163,235,359,08h 
    
notun_notun_block_banao:
        
        ;cmp [block_boshche],1
        ;jne notun_notun_block_banao
        ;mov [block_boshche],0
        ;show_next_piece horizontal
        ;copy horizontal array to currentBlock
        
        inc [current_block]
        cmp [current_block],3
        jle continue_kor
        
        mov [current_block],1
    
        continue_kor:
        
            call gen_block
      
            update_block choose_random_piece, currentBlock
            
            call gen_next_piece
            call show_next_piece
            
            time_delay currentBlock
                 
            call hawahawaline 
            
            
            
            call score_dekhao
            call gameover
            cmp seshs,23
            je seshh
            add color,5
            add next_color,5
            cmp color,14
            jg Ooops
            
            cmp next_color,14
            jg Ooops_next
            
            jmp notun_notun_block_banao
Ooops:  
        mov color,4
        jmp notun_notun_block_banao
        
Ooops_next:  
        mov next_color,4
        jmp notun_notun_block_banao
seshh:
    
   mov ah,0
   mov al,13h
   int 10h
      
   ; *** SUA LOI: Vo hieu hoa ngat khong duoc ho tro ***
   ; mov ah,0bh
   ; mov bh,0
   ; mov bl,10
   ; int 10h


   display_string msg_game_over ,10,15,10,2 
    display_string msg_game_over ,10,15,10,2
     display_string msg_game_over ,10,15,10,2
      display_string msg_game_over ,10,15,10,2
      
    
   jmp seshh
         
   MAIN ENDP


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; all procedures ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; draw screen elements 

procedure_draw_screen proc near
    
    draw_screen_border:
        
        ; --- SUA TOA DO X (chia 2) CHO MODE 13h (320-wide) ---
        ;top left to top right
        draw_row 5,5,315,03h ; (10,630) -> (5,315)
        ;top left to bottom left
        draw_column 5,5,195,03h ; (10) -> (5)
        ;top right to bottom right
        draw_column 315,5,195,03h ; (630) -> (315)
        ;bottom left to bottom right
        draw_row 195,5,315,03h ; (10,630) -> (5,315)
        
    
    draw_screen_play_area:
        
        ; --- SUA TOA DO X (chia 2) ---
        ;top left to top right
        draw_row 42,114,190,7 ; (228,381) -> (114, 190)
        ;top left to bottom left
        draw_column 114,42,165,7 ; (228) -> (114)
        ;top right to bottom right
        draw_column 190,42,165,7 ; (381) -> (190)
        ;bottom left to bottom right
        draw_row 165,114,190,7 ; (228,381) -> (114, 190)
        
        
    draw_screen_next_piece:
        
        ; --- SUA TOA DO X (chia 2) ---
        ;top left to top right
        draw_row 50,200,244,01h ; (400,487) -> (200, 244)
        ;top left to bottom left
        draw_column 200,50,90,01h ; (400) -> (200)
        ;top right to bottom right
        draw_column 244,50,90,01h ; (487) -> (244)
        ;bottom left to bottom right
        draw_row 90,200,244,01h ; (400,487) -> (200, 244)
        
    
    draw_screen_strings:
        
        ; --- SUA TOA DO X (chia 2) cho cac string ---
        ; (row, col)
        display_string msg_left,10,5,8,9     ; (col 10 -> 5)
        display_string msg_right,12,5,9,12    ; (col 10 -> 5)
        display_string msg_rotate,14,5,13,8   ; (col 10 -> 5)
        
        display_string msg_tetris,3,17,6,6  ; (col 35 -> ~17)
        
        ; Toa do cot Text mode = Toa do Pixel / 8
        ; (400) -> 200 / 8 = cot 25
        ; (54 * 8 = 432) -> 216 / 8 = cot 27
        display_string msg_next,12,27,4,8   ; (col 54 -> 27)
        display_string msg_score,18,26,5,9  ; (col 53 -> ~26)
        display_string game_score,16,26,4,8 ; (col 53 -> ~26)
        
        ret
    
procedure_draw_screen endp



setup_int Proc
;    save old vector and set up new vector
;    input: al = interrupt number
;    di = address of buffer for old vector
;    si = address of buffer containing new vector
;    save old interrupt vector

    MOV AH, 35h     ; get vector
    INT 21h
    MOV [DI], BX    ; save offset
    MOV [DI+2], ES  ; save segment
          
;   setup new vector

    MOV DX, [SI]    ; dx has offset
    PUSH DS         ; save ds
    MOV DS, [SI+2]  ; ds has the segment number
    MOV AH, 25h     ; set vector
    INT 21h
    POP DS
    RET
setup_int EndP


timer_tick Proc
    PUSH DS
    PUSH AX
    
    MOV AX, Seg timer_flag
    MOV DS, AX
    MOV timer_flag, 1
    
    ; --- THEM 2 DONG SUA LOI O DAY ---
    MOV AL, 20h ; Gui tin hieu EOI (End of Interrupt)
    OUT 20h, AL ; den cong 20h cua chip PIC
    
exit:    
    POP AX
    POP DS
    
    IRET
timer_tick EndP




move_block Proc
;   erase block at current position and display at new position
;   input: CX = col of block position
;   DX = rwo of block position
;   erase block
;   MOV AL, 0
;   mov bx,300
;   mov cx,310
;   push ax

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;keyboard bae
 
;   mov ah, 1 ;keyboar buffer check korbe
    mov ah, 1 ;keyboar buffer check korbe
    int 16h
;   int 16h
    jz foo
    mov ah, 0    ; key input nibe
    int 16h 
    cmp al,97 ; a checker
    je keya
    cmp al,100 ; d checker
    je fix2
    cmp al,115
    je dours
    foo: jmp boo
    
    keya:
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
      
        xor cx,cx
        xor dx,dx
        mov cx,currentBlock[20]
        sub cx,45
        mov dx,currentBlock[16]
fix1:   
        jmp fix3
fix2:
        jmp keyd
dours: jmp dour
fix3:
      
        ; xor ax,ax
        ;  mov dx,158
        ;  mov cx,301
        mov ah,0dh
        
        
        int 10h
        cmp al,09h
        je boo
        cmp al,0eh
        je boo
        cmp al,04h
        je boo
        add dx,10
        int 10h
        cmp al,0eh
        je boo
        cmp al,09h
        je boo
        cmp al,04h
        je boo
      
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        draw_full_block currentBlock,15 , 24
        modify_column_elementsA currentBlock,30,30
        
    boo:    jmp exittt
    
    dour:  
          jmp exitttt
    
    keyd: 
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        xor cx,cx
        xor dx,dx
        mov cx,currentBlock[20]
        add cx,15
        mov dx,currentBlock[16]
        
        ; xor ax,ax
        ;  mov dx,158
        ;  mov cx,301
        mov ah,0dh
        
        
        int 10h
        cmp al,09h
        je exittt
        cmp al,0eh
        je exittt
        cmp al,04h
        je exittt
        
        add dx,10
        int 10h
        cmp al,09h
        je exittt
        cmp al,0eh
        je exittt
        cmp al,04h
        je exittt
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    draw_full_block currentBlock,15 , 30
    modify_column_elementsD currentBlock,30,30
         jmp exittt
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;muhahaha hoya gese  


    
exittt:    
    
      draw_full_block currentBlock,15, 24
      
     ;draw_full_block vertical,15
     ;draw_full_block L_shape,15
  
       jmp test_timer
      
     ;   draw_block boxer_a,boxer_b,320,330,15
     ;   draw_block boxer_a,boxer_b,332,342,15
     ;   draw_block boxer_a,boxer_b,344,354,15
    
     ;   get new position  
     ;   check boundary
     ;   cmp cx,160
     ;   jl exits
     ;   CALL 
     
     ;   wait for 1 timer tick to display block
     
   exitttt:
    
  draw_full_block currentBlock,15, 24
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        xor cx,cx
        xor dx,dx
        mov cx,currentBlock[4]
        inc cx
        ;   add cx,20
        mov dx,currentBlock[16]
        
         xor ax,ax
        ;  mov dx,158
        ;  mov cx,301
           mov ah,0dh
        
        cmp dx,140
        jg test_timer 
        add dx,24
        
        int 10h
        cmp al,09h
        je test_timer
        cmp al,0eh
        je test_timer
        cmp al,04h
        je test_timer
        add cx,20
        int 10h
        cmp al,09h
        je test_timer
        cmp al,0eh
        je test_timer
        cmp al,04h
        je test_timer
    ;   add cx 20
      
        ; add dx,10
        ;int 10h
        ; cmp al,09h
        ;  je exittt
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        modify_row_elements currentBlock,12, 4
    jmp test_timer
 
test_timer:
    
    xor ax,ax
    ; --- SUA LOI: Xoa 2 dong bi lap vo han duoi day ---
    ; CMP timer_flag, 1
    ; JNE test_timer
    
    modify_row_elements currentBlock,6 ,16
    
    draw_full_block currentBlock,color,24
   ; modify_row_elements vertical
   ; modify_row_elements L_shape
   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;  push ax
        ;  push cx
        ;  push dx
        xor cx,cx
        xor dx,dx
        mov cx,currentBlock[4]
        inc cx
        ;    ; add cx,
        mov dx,currentBlock[16]
        add dx,10
        ; xor ax,ax
        ;  mov dx,158
        ;  mov cx,301
        mov ah,0dh
        
        
        int 10h
        cmp al,09h
        je exits2
        cmp al,0eh
        je exits2
        cmp al,04h
        je exits2
        
        add cx,20
      
        int 10h
        cmp al,09h
        je exits2
        cmp al,0eh
        je exits2
        cmp al,04h
        je exits2   
 
      ; jne exits
                
            
      ;   pop dx
      ;   pop cx
      ;   pop ax
          
      ;   jne exits2
            
      ;   exits2:
      ;   mov currentBlock[18],160
      ;   RET
      
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
      ;   halum:    
      
      ;draw_full_block currentBlock,09h
      
   ;  draw_full_block vertical,08h
   ;  draw_full_block L_shape,08h
    
    
    ;draw_block boxer_a,boxer_b,320,330,08h
    ;draw_block boxer_a,boxer_b,332,342,08h
    ;draw_block boxer_a,boxer_b,344,354,08h
    ;
    
    MOV timer_flag, 0
   ; MOV AL, 3
    
    exits:
    
        RET
        
    exits2:
    
    ; mov cx,170

    ; draw_full_block currentBlock,09h
    mov currentBlock[16],170
    
    RET
    
    ;dec cx
      
        
        
move_block EndP


hawahawaline Proc
  ;  push dx
  ;;  push cx
  ;  push bx
   ; push ax
   xor ax,ax
   xor bx,bx
   xor cx,cx
   xor dx,dx
    
hambahamba:
    
      mov ah,0dh
    
      mov a1,164
      mov b1,56
      mov a2,115 ; *** SUA: 230 -> 115 ***
      mov b2,120 ; *** SUA: 240 -> 120 ***
      
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    
    
      mov line,170
   ;    mov dx,line
khuru:
      mov cx,117 ; *** SUA: 235 -> 117 ***
      sub line,6
      mov dx,line
      mov a1,dx
dhuru:
    add cx,10
    cmp cx,190 ; *** SUA: 380 -> 190 ***
    jg prehh1
    xor ax,ax
    mov ah,0dh    
    int 10h
    cmp al,09h
    je dhuru
    cmp al,0eh
    je dhuru
    cmp al,04h
    je dhuru
    jmp hh3
    
prehh1:
      add score,10
   hh1:
    
    mov a2,110 ; *** SUA: 220 -> 110 ***
    sub a1,6
   hh2:
    
    cmp a1,55
    jl hh3
    
    add a2,10
    cmp a2,185 ; *** SUA: 370 -> 185 ***
    jg hh1
    
    mov bx,a1
    add bx,6
    mov b1,bx
    
    mov bx,a2
    add bx,10
    mov b2,bx
    xor ax,ax
    xor bx,bx
    xor cx,cx
    xor dx,dx
    mov cx,a2
    inc cx
   ; add cx,15
    mov dx,a1
    sub dx,4
    mov ah,0dh
    int 10h
    draw_block a1,b1,a2,b2,al  ;0 hobe kaj korle
    jmp hh2
    
hh3: 
    mov a2,110 ; *** SUA: 220 -> 110 ***
    cmp line,60
    jl fillhoynai
    jmp khuru
fillhoynai:
;mov ah,4ch
   ;   int 21h
   ; pop ax
   ;  pop bx
   ;  pop cx
   ;  pop dx
    RET
hawahawaline Endp


score_dekhao proc
        
        push ax
        push bx
        push cx
        push dx
        
        
        mov cx,10d
        xor bx,bx
        mov bx,3
        mov ax,score
        
        bhag_kor:
            
            xor dx,dx
            div cx
            
            ;push bx
            ;inc cx
            
            or dl,30h
            mov game_score[bx],dl
            dec bx
            
            
            or ax,ax
            jne bhag_kor
            
        
       

         display_string game_score,16,26,4,8 ; *** SUA: cot 53 -> 26 ***
         
         
         pop dx
         pop cx
         pop bx
         pop ax
        
       
         ret


score_dekhao Endp


gen_block proc

    cmp [current_block],1
    je horizontal_ako
    
    cmp [current_block],2
    je L_shape_ako
      
    cmp [current_block],3
    je right_L_ako
    
    
    horizontal_ako:
            update_block horizontal, choose_random_piece
            mov [next_block],2
            ret
    
            
    L_shape_ako:
            update_block L_shape, choose_random_piece
            mov [next_block],3
            ret
                
    right_L_ako:
               update_block right_L, choose_random_piece
               mov [next_block],1
               ret
      
    
    ret 
    
gen_block endp


gen_next_piece proc
    
    cmp [next_block],1
    je horizontal_akao
    
    cmp [next_block],2
    je L_shape_akao
    
    cmp [next_block],3
    je right_L_akao
    
   
    horizontal_akao:
            update_block next_horizontal, next_piece
            ret
            
    L_shape_akao:
            update_block next_L_shape, next_piece
            ret
            
    right_L_akao:
               update_block next_right_L, next_piece
               ret

         
    ret 


gen_next_piece endp


show_next_piece proc ;pattern_name - konta next piece box e dekhano hobe 
    
        push bx
        push cx
        push dx
        
        ; *** SUA: Toa do X (cot) chia 2 ***
        draw_block 61,89,200,235,0Fh ; (401, 470) -> (200, 235)
        

    ;   ;add_offset_array 
    ;                      ;pasher picchi box e dekhanor jonno
    ;   mov bx,0
    ;   mov cx,16
    ;   
    ;           
    ;   jog_koro:
    ;         mov dx,next_piece[bx]
    ;         add dx,offsetArray[bx]
    ;         
    ;         mov temp_nxt_piece[bx],dx
    ;         add bx,2
    ;         xor dx,dx
    ;         loop jog_koro
    ;         
    ;   ;draw_full_block next_piece
      
            draw_full_block next_piece, [next_color], 24
      ;    update_to_zero temp_nxt_piece
      ;    update_to_zero next_piece
      
      pop dx
      pop cx
      pop bx
      
      ret
      
show_next_piece endp


update_to_zero macro input
    local zero_banao

    push bx
    push cx
    
    mov bx,0
    mov cx,16
    
    zero_banao:
            mov input[bx],0
            add bx,2
            loop zero_banao
    

    EndM


;keyboard strike


gameover proc
    xor ax,ax
    xor cx,cx
    xor dx,dx
    mov dx,59
    mov cx,148 ; *** SUA: 297 -> 148 ***
    mov ah,0dh
    int 10h
    cmp al,09h
    je sesh1
    cmp al,04h
    je sesh1
    cmp al,0eh
    je sesh1
    
   
    sesh: RET
    
    sesh1:
    
    
   ; *** SUA LOI: Vo hieu hoa ngat khong duoc ho tro ***
   ; mov ah,0bh
   ; mov bh,1
   ; mov bl,13
   ; int 10h
   mov seshs,23
   RET
     
    
gameover endp
End main