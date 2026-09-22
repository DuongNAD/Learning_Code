.model small
.stack 100  


.data

    p_a     db  'Nhap so a(0-9): '
    p_b     db  13, 10, 'Nhap so b (0-9): $'
    p_sum   db  13, 10, 'Tong = $'
    p_err   db  13, 10, 'Loi: Ban phai nhap so tu 0 den !$' 
    
    so_a    db

.code
main proc
    
    mov ax, @data
    mov ds, ax
    
    mov ah, 9 
    lea dx, p_a
    int 21h
    
    mov ah, 1 
    int 21h
    
    cmp al, '0'
    jl loi_nhap
    cmp al
    
    main endp