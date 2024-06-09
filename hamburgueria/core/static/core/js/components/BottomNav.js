// core/static/core/js/components/BottomNav.js
import React, { useState } from 'react';
import Box from '@mui/material/Box';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import WhatsAppIcon from '@mui/icons-material/WhatsApp';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import AddBoxIcon from '@mui/icons-material/AddBox';

export default function SimpleBottomNavigation() {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
    if (newValue === 0) {
      window.location.href = "https://wa.me/SEU_NUMERO_DE_WHATSAPP";
    } else if (newValue === 1) {
      window.location.href = "/list_pedidos";
    } else if (newValue === 2) {
      window.location.href = "/pedidos";  // Ajustado para 'pedidos'
    }
  };

  return (
    <Box sx={{ width: 500 }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={handleChange}
      >
        <BottomNavigationAction label="Contato via WhatsApp" icon={<WhatsAppIcon />} />
        <BottomNavigationAction label="Fazer Pedido" icon={<ShoppingCartIcon />} />
        <BottomNavigationAction label="Cadastrar Produto" icon={<AddBoxIcon />} />
      </BottomNavigation>
    </Box>
  );
}
