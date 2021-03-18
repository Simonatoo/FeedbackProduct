import React from 'react'
import './styles/PrincipalItem.css'

function PrincipalItem(){

    var url_image = "https://assets.instabuy.com.br/ib.item.image.big/b-6a125e517c7f420c9fcda0f5f534f500.jpeg"

    return(
        <div className="main-body">
            <div className="main-margem">
                <div className="main-image">
                    <img src={url_image} alt="" width="100%"/>
                </div>
                <div className="main-rating-body">
                    <div className="main-rating">
                        <h1>
                            4.99
                        </h1>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default PrincipalItem