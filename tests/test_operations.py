import pytest
# Import functions directly from the base12math package
from base12math import to_base12, from_base12, add12, mul12

# --- Tests for to_base12 ---

def test_to_base12_zero():
    assert to_base12(0) == "0"

def test_to_base12_single_digits():
    assert to_base12(5) == "5"
    assert to_base12(10) == "T"
    assert to_base12(11) == "E"

def test_to_base12_multiple_digits():
    assert to_base12(12) == "10"
    assert to_base12(25) == "21"
    assert to_base12(144) == "100"
    assert to_base12(131) == "TE" # 10*12 + 11
    assert to_base12(2023) == "1207" # Corrected based on manual calculation

def test_to_base12_invalid_input():
    with pytest.raises(ValueError, match="non-negative integer"):
        to_base12(-1)
    with pytest.raises(ValueError, match="non-negative integer"):
        to_base12(10.5)
    with pytest.raises(ValueError, match="non-negative integer"):
        to_base12("abc")

# --- Tests for from_base12 ---

def test_from_base12_zero():
    assert from_base12("0") == 0

def test_from_base12_single_digits():
    assert from_base12("5") == 5
    assert from_base12("T") == 10
    assert from_base12("E") == 11
    assert from_base12("t") == 10 # Case-insensitive
    assert from_base12("e") == 11 # Case-insensitive

def test_from_base12_multiple_digits():
    assert from_base12("10") == 12
    assert from_base12("21") == 25
    assert from_base12("100") == 144
    assert from_base12("TE") == 131 # 10*12 + 11
    assert from_base12("1207") == 2023 # Corrected based on calculation above
    assert from_base12("   1T ") == 22 # Test stripping whitespace, changed A to T

def test_from_base12_invalid_input():
    with pytest.raises(ValueError, match="non-empty string"):
        from_base12("")
    with pytest.raises(ValueError, match="Invalid duodecimal digit: 'G'"):
        from_base12("1G")
    with pytest.raises(ValueError, match="Invalid duodecimal digit: '.'"):
        from_base12("1.0")
    with pytest.raises(ValueError, match="non-empty string"):
        from_base12(123)

# --- Tests for add12 ---

def test_add12_simple():
    assert add12("1", "1") == "2"
    assert add12("5", "5") == "T"
    assert add12("T", "1") == "E"
    assert add12("E", "1") == "10"
    assert add12("0", "5") == "5"
    assert add12("5", "0") == "5"

def test_add12_carry():
    assert add12("9", "3") == "10"
    assert add12("T", "T") == "18" # 10+10=20 -> 1*12+8
    assert add12("E", "E") == "1T" # 11+11=22 -> 1*12+10
    assert add12("1E", "1") == "20" # 23+1=24 -> 2*12+0
    assert add12("TE", "12") == "101" # Corrected: 131 + 14 = 145 -> 1*144 + 0*12 + 1
    assert add12("1T", "2E") == "49" # Changed A->T, B->E: 22 + 35 = 57 -> 4*12 + 9
    assert add12("EEE", "1") == "1000" # 1727 + 1 = 1728

# --- Tests for mul12 ---

def test_mul12_simple():
    assert mul12("1", "5") == "5"
    assert mul12("2", "6") == "10" # 2*6=12
    assert mul12("T", "1") == "T"
    assert mul12("E", "0") == "0"
    assert mul12("0", "E") == "0"

def test_mul12_carry():
    assert mul12("3", "4") == "10" # 3*4=12
    assert mul12("5", "5") == "21" # 5*5=25 -> 2*12+1
    assert mul12("T", "T") == "84" # 10*10=100 -> 8*12+4
    assert mul12("E", "E") == "T1" # 11*11=121 -> 10*12+1
    assert mul12("11", "11") == "121" # 13*13=169 -> 1*144 + 2*12 + 1
    assert mul12("20", "T") == "180" # Changed A to T: 24 * 10 = 240 -> 1*144 + 8*12 + 0
    assert mul12("1T", "2E") == "542" # Changed A->T, B->E: 22 * 35 = 770 -> 5*144 + 4*12 + 2
    assert mul12("TE", "12") == "108T" # 131 * 14 = 1834 -> 1*1728 + 0*144 + 8*12 + 10
