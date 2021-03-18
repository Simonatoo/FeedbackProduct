import React from 'react'
import './styles/input-search.css'

function Input(){
    return(
        <div>
            <div className="title">
                <h1><b>Busque seu produto</b> abaixo</h1>
                <p>Busque seu produto abaixo</p>
            </div>
            <div className="input-search">
                <form className="input-body" action="">
                    <input className="input-text" type="text"/>
                    <input className="input-button" type="submit" value="Buscar"/>
                </form>
            </div>
        </div>
    )
}

export default Input