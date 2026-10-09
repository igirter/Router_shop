import './ProductCard.css'

export function ProductCard({ product, onOrder }) {
  const { name, description, price } = product

  return (
    <article className="product-card">
      <div className="product-card__image-wrapper">
        <span>Фото товара</span>
      </div>

      <div className="product-card__content">
        <h3 className="product-card__title">
          {name}
        </h3>

        <p className="product-card__description">
          {description}
        </p>

        <div className="product-card__footer">
          <span className="product-card__price">
            {price.toLocaleString('ru-RU')} ₽
          </span>

          <button
            className="product-card__button"
            type="button"
            onClick={() => onOrder(product)}
          >
            Заказать
          </button>
        </div>
      </div>
    </article>
  )
}