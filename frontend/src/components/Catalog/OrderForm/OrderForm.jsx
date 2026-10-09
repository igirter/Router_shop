import { useState } from 'react'

import './OrderForm.css'

export function OrderForm({ product, onClose }) {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    address: '',
  })

  const handleChange = (event) => {
    const { name, value } = event.target

    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }))
  }

  const handleSubmit = async (event) => {
    console.log('HANDLE SUBMIT')

    event.preventDefault()

    const orderData = {
      full_name: formData.name,
      phone: formData.phone,
      email: formData.email,
      address: formData.address,

      products: [
        {
          product_id: product.id,
          count: 1,
        },
      ],
    }

    console.log('ПЕРЕД FETCH')

    const response = await fetch('/api/checkouts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(orderData),
    })

    console.log(response)
  }

  return (
    <div className="order-modal">
      <div
        className="order-modal__overlay"
        onClick={onClose}
      />

      <div className="order-form">
        <div className="order-form__header">
          <h3 className="order-form__title">
            Оформление заказа
          </h3>

          <button
            className="order-form__close"
            type="button"
            onClick={onClose}
            aria-label="Закрыть форму"
          >
            ×
          </button>
        </div>

        <div className="order-form__product">
          <span className="order-form__product-name">
            {product.name}
          </span>

          <span className="order-form__product-price">
            {product.price.toLocaleString('ru-RU')} ₽
          </span>
        </div>

        <form
          className="order-form__form"
          onSubmit={handleSubmit}
        >
          <label className="order-form__field">
            <span>ФИО</span>

            <input
              type="text"
              name="name"
              placeholder="Введите ваше ФИО"
              onChange={handleChange}
              required
            />
          </label>

          <label className="order-form__field">
            <span>Email</span>

            <input
              type="email"
              name="email"
              placeholder="Введите email"
              onChange={handleChange}
              required
            />
          </label>

          <label className="order-form__field">
            <span>Телефон</span>

            <input
              type="tel"
              name="phone"
              placeholder="+7 (___) ___-__-__"
              onChange={handleChange}
              required
            />
          </label>

          <label className="order-form__field">
            <span>Адрес</span>

            <input
              type="text"
              name="address"
              placeholder="Введите адрес доставки"
              onChange={handleChange}
              required
            />
          </label>

          <button
            className="order-form__submit"
            type="submit"
          >
            Заказать
          </button>
        </form>
      </div>
    </div>
  )
}